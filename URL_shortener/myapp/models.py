from django.db import models

# Create your models here.
class LongToShort(models.Model):
    long_url = models.URLField(max_length=600)
    short_url = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)  ## automatically added when created at first
    clicks = models.IntegerField(default=0)
    country_clicks = models.JSONField(default=dict)  # {'country_name': click_count}
    device_clicks = models.JSONField(default=dict)  # {'device_type': click_count}