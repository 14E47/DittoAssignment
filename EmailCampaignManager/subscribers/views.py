from django.shortcuts import render
from .models import Subscriber
from .forms import SubscribeForm, UnsubscribeForm
from django.http import HttpResponse
import logging


# Create your views here.
def home(request):
    return render(request, 'subscribers/home.html',)


def subscribeform(request):
    form = SubscribeForm()
    return render(request, 'subscribers/subscribe_form.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            try:
                # if subscriber email already present, mark active
                obj = Subscriber.objects.get(email=email)
                obj.active = True
                obj.save()
            except:
                # if subscriber not present, create new subscriber
                Subscriber.objects.get_or_create(first_name=first_name, email=email)
    return render(request, 'subscribers/subscribe.html')


def unsubscribeform(request):
    form = UnsubscribeForm()
    return render(request, 'subscribers/unsubscribe_form.html', {'form': form})


def unsubscribe(request):

    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                obj = Subscriber.objects.get(email=email)
                obj.active = False
                obj.save()
            except:
                return render(request, 'subscribers/unsubscribe_404.html')
    return render(request, 'subscribers/unsubscribe.html')

