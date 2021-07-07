from django.shortcuts import render
from .models import Campaign
from EmailCampaignManager.subscribers.models import Subscriber
import threading
import time


# Create your views here.
def get_all_active_subscribers(request):
    active_subscribers = Subscriber.objects.filter(active=True)
    return active_subscribers


def create_mailer(request):

    email_ids = []
    all_active_subscribers = get_all_active_subscribers()
    for i in all_active_subscribers:
        email_ids.append(i.email)

    email = None
    if request.method == 'POST':
        slug = request.POST.get('slug')
        campaign_data = Campaign.objects.get(slug=slug)

        # create dynaic html email template with campaign data, leaving right now
        email = campaign_data

    return send_emails(email, email_ids)


def schedule_email(request):

    threads = 10
    jobs = []
    for i in range(0, threads):
        t = threading.Thread(target=send_emails)
        jobs.append(t)

    # Start threads
    for j in jobs:
        j.start()
        time.sleep(5)

    # join threads
    for j in jobs:
        j.join()

    return "Success"


#TODO
def send_emails(request, email, email_ids):
    pass
