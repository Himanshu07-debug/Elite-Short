from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world),   ## localhost:8000/hello
    path('', views.home_page),
    path('all-analytics',views.all_analytics),
    path('analytics/<slug:short_url>', views.analytics_view),
    path('<slug:short_url>', views.redirect_url)
]
