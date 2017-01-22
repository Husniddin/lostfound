from django.contrib import admin

# Register your models here.
from .models import LostAds
from .forms import LostAdsForm

class LostAdsAdmin(admin.ModelAdmin):
	list_display=["title", "text", "email", "created_dt"]
	form = LostAdsForm
	# class Meta:
	# 	model=LostAds
	
		
admin.site.register(LostAds, LostAdsAdmin)