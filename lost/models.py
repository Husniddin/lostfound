from django.db import models
# from datetime import date
from django.utils import timezone

class LostAds(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    text = models.TextField()
    created_dt = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    # created_dt = models.DateTimeField(auto_now=True, auto_now_add=True, default=timezone.now(), null=True, blank=True)
    # created_dt = models.DateField(auto_now=False, auto_now_add=True, default=date.today(), null=True, blank=True)

    def __str__(self):
    	return self.title
