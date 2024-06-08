from django.shortcuts import render, redirect
import os

## import http
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings

from .models import LongToShort

from URL_shortener.settings import BASE_DIR

p = os.path.join(BASE_DIR, "templates")

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world!")

# Helper function to determine country and device type
def get_country_and_device(request):
    country = "India"
    device = "Desktop"
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    if 'mobile' in user_agent:
        device = "Mobile"

    ip_address = request.META.get('REMOTE_ADDR', None)
    if ip_address:
        try:
            g = GeoIP2()
            country = g.country(ip_address)['country_name']
        except Exception as e:
            print(f"GeoIP2 error: {e}")

    return country, device

    ## remember - localhost is not there in geoip database, it will required Public address



def home_page(request):
    
    # request.method --> to know GET / POST 
    
    context = {
        "submitted" : False,
        "error" : False
    }
    
    if request.method == 'POST':
        
        data = request.POST   ## data --> dictionary
        long_url = data['longurl']
        custom_name = data['custom_name']
        # print(long_url, custom_name)
        
        try:
            ## insertion in Database
            obj = LongToShort(long_url = long_url, short_url = custom_name)
            obj.save()
            
            ## Reading from the current database
            date = obj.date
            clicks = obj.clicks
            
            ## adding the short_url and long_url in the context body
            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name          
            ## to get the current tab uri and appneding in it the custom name
            context["date"] = date
            context["clicks"] = clicks
            
            context["submitted"] = True   ## show the box
        except:
            context["error"] = True
        
    
    return render(request,"index.html", context)

## Redirecting from short_url to original long_url when user clicks it
def redirect_url(request, short_url):
    ## searching in the DB
    row = LongToShort.objects.filter(short_url = short_url)
    
    if len(row) == 0:
        return HttpResponse("No such url exist")
    
    obj = row[0]
    long_url = obj.long_url
    
    obj.clicks = obj.clicks + 1
    
    country, device = get_country_and_device(request)
    
    if country in obj.country_clicks:
        obj.country_clicks[country] += 1
    else:
        obj.country_clicks[country] = 1
    
    if device in obj.device_clicks:
        obj.device_clicks[device] += 1
    else:
        obj.device_clicks[device] = 1
    
    obj.save()
    
    ## Redirecting to long_url
    return redirect(long_url)


def analytics_view(request, short_url):
    obj = LongToShort.objects.get(short_url = short_url)
    
    # Prepare data for charts
    countries = list(obj.country_clicks.keys())
    clicks = list(obj.country_clicks.values())
    desktop = obj.device_clicks.get('Desktop', 0)
    mobile = obj.device_clicks.get('Mobile', 0)
    
    base_url = request.build_absolute_uri().split('/analytics')[0]
    link = f"{base_url}/{obj.short_url}"
    
    context = {
        'date': obj.date,
        'long_url': obj.long_url,
        'short_url': short_url,
        'total_clicks': obj.clicks,
        'countries': countries,
        'clicks': clicks,
        'desktop': desktop,
        'mobile': mobile,
        'link':link
    }
    
    # print(context['short_url'])
    
    return render(request, 'analytics.html', context)


def all_analytics(request):
    
    row = LongToShort.objects.all()
    
    for obj in row:
        # Extract the base URL
        base_url = request.build_absolute_uri().split('/all-analytics')[0]
        # Append the required part to create the analytics URL
        obj.analytics_url = f"{base_url}/analytics/{obj.short_url}"
    
    context = {
        "rows" : row
    }
    
    return render(request, "all-analytics.html", context)




