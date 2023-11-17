from django.shortcuts import render
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from payment.models import Product, StripeCustomer
from django.http.response import JsonResponse
import stripe
from django.conf import settings
from datetime import datetime
# Create your views here.


def home(request):

    return render(request, 'main/index.html')


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
