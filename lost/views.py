from django.conf import settings

from django.shortcuts import render

from django.http import HttpResponse

from .forms import LostAdsForm, ContactForm

from django.core.mail import send_mail


def index(request):
    return HttpResponse("Hello world from lost")


def home(request):
    title = "Hello world %s" % (request.user)
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

    # return render(request, 'lost/home.html', context)
    return render(request, 'lost/main.html', context)


def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')
        # send_mail('Site contact form', message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=True)

    context = {
        "form": form
    }

    return render(request, 'lost/contact.html', context)
