from django.shortcuts import render

from django.http import HttpResponse

from .forms import LostAdsForm


def index(request):
    return HttpResponse("Hello world from lost")


def home(request):
	title = "Hello world %s" %(request.user)
	form = LostAdsForm(request.POST or None)

	context = {
		"title": title,
		"form": form,
	}

	if request.method == 'POST':
		print(request.POST)



	if form.is_valid():

		instance = form.save(commit=False)

		# Validatsiyadan o'tadi.
		email = form.cleaned_data.get('email')
		if not email:
			email = "myemail@gmail.com"
			instance.email = email

		if not instance.title:
			instance.title = 'Hello world 8888'

		instance.save()
		context = {
			"title": 'Thank you',
		}

	return render(request, 'lost/home.html', context)
