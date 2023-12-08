from django.shortcuts import render, redirect
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from payment.models import Product, StripeCustomer
from django.http.response import JsonResponse
import stripe
from django.conf import settings
from datetime import datetime
from lotus.models import Article

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('app')
    else:
        stripe_list = Product.objects.all()
        artical = Article.objects.all()[:3]

        return render(request, 'main/index.html', {
            'product_list': stripe_list,
            'article_list':artical
        })

def features(request):
    return render(request, 'main/features.html')

def knowledgebase(request):
    return render(request, 'main/knowledgebase.html')

def about(request):

    return render(request, 'main/about.html')


def pricing(request):

    return render(request, 'main/pricing.html')


def team(request):

    return render(request, 'main/index.html')


def contact(request):

    return render(request, 'main/contact.html')


def blog(request):

    return render(request, 'main/blog.html')


def blog_artical(request):

    return render(request, 'main/blog-artical.html')


def How_it_works(request):

    return render(request, 'main/how-it-works.html')


def privacy(request):

    return render(request, 'main/privacy.html')


def terms(request):

    return render(request, 'main/terms.html')


def refund(request):

    return render(request, 'main/refund.html')

# def home(request):
#     try:
#         # Retrieve the subscription & product
#         stripe_customer = StripeCustomer.objects.get(user=request.user)
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         subscription = stripe.Subscription.retrieve(
#             stripe_customer.stripeSubscriptionId)
#         product = stripe.Product.retrieve(subscription.plan.product)

#         start_timestamp = subscription['current_period_start']
#         end_timestamp = subscription['current_period_end']
#         start_time = datetime.fromtimestamp(start_timestamp)
#         end_time = datetime.fromtimestamp(end_timestamp)

#         subscription['current_period_start'] = start_time
#         subscription['current_period_end'] = end_time

#         # return JsonResponse({
#         #     'subscription': subscription,
#         #     'product': product,
#         # })
#         return render(request, 'index.html', {
#             'subscription': subscription,
#             'product': product,
#         })

#     except:
#         stripe_list = Product.objects.all()

#         return render(request, 'index.html', {
#             'product_list': stripe_list
#         })


def verification_email(request, *args, **kwargs):

    if "action_send" in request.POST:
        email = request.POST["email"]
        email_address = None
        try:
            email_address = EmailAddress.objects.get_for_user(
                user=request.user, email=email)
        except EmailAddress.DoesNotExist:
            pass
        if email_address:
            send_email_confirmation(
                request, request.user, email=email_address.email
            )
            content = {
                'status': 'done'
            }
            return render(request, "index.html", content)

    return render(request, "index.html")



def ticket(request, *args, **kwargs):
    if request.POST:

        email_me = 'support@ziko.ai'

        full_name=request.POST["full_name"]
        Email=request.POST["email"]
        Phone=request.POST["phone"]
        Message=request.POST["message"]

        subject = 'This is a ticket created by the customer'
        
        full_mess = f"""

Full name : {full_name}
Email : {Email}
Phone : {Phone}
Message : {Message}
"""
        email_from = email_me
        recipient_list = ['support@ziko.ai', ]
        send_mail( subject, full_mess, email_from, recipient_list )

        return redirect('home')
    else:
        return redirect('home')