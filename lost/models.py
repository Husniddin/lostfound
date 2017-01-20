from django.db import models

class LostAds(models.Model):
    ads_title = models.CharField(max_length=255, null=True, blank=True)
    ads_text = models.TextField()
