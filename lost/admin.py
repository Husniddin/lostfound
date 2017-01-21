from django.contrib import admin

# Register your models here.
from .models import LostAds

class LostAdsAdmin(admin.ModelAdmin):
	list_display=["title", "text", "email", "created_dt"]
	class Meta:
		model=LostAds
	
		
admin.site.register(LostAds, LostAdsAdmin)