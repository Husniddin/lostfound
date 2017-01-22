from django import forms

from .models import LostAds

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


class LostAdsForm(forms.ModelForm):
	class Meta:
		model = LostAds
		fields = ['title', 'email', 'text']

	def clean_email(self):
		# print(self.cleaned_data.get('email'))
		# raise forms.ValidationError('Email error')
		# return 'hello@gmail.com'
		return self.cleaned_data.get('email')

	def clean_text(self):
		return self.cleaned_data.get('text')