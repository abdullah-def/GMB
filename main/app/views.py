from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # import messages
from django.contrib.auth.models import User
# Create your views here.

from payment.models import Product, StripeCustomer
from accounts.models import Profile
from allauth.account.forms import ChangePasswordForm


@login_required
def home(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/index.html', {
        'product_list': stripe_list
    })
    # return render(request, 'app/index.html')


@login_required
def reviews(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/reviews.html', {
        'product_list': stripe_list
    })


@login_required
def settings(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/settings.html', {
        'product_list': stripe_list
    })
    # return render(request, 'app/index.html')


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    myform = ChangePasswordForm()
    return render(request, 'app/profile.html', {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_numer': profile.phone_numer,
        'country': profile.country,
        'city': profile.city,
        'address': profile.address,
        'website': profile.website,
        'form': myform,
    })
    # return render(request, 'app/index.html')


@login_required
def plans(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/plans.html', {
        'product_list': stripe_list
    })
    # return render(request, 'app/index.html')


@login_required
def accounts(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/accounts.html', {
        'product_list': stripe_list
    })


@login_required
def profile_edit(request):
    if request.POST:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id=request.user.id)

        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        phone_numer = request.POST['phone_numer'].strip()
        country = request.POST['country'].strip()
        city = request.POST['city'].strip()
        address = request.POST['address'].strip()
        website = request.POST['website'].strip()

        if first_name:
            try:
                user.first_name = first_name
                user.save()
                messages.success(request, "First Name successfully changed.")
            except:
                messages.error(request, "First Name change failed.")

        if last_name:
            try:
                user.last_name = last_name
                user.save()
                messages.success(request, "Last Name successfully changed.")
            except:
                messages.error(request, "Last Name change failed.")

        if phone_numer:
            try:
                profile.phone_numer = phone_numer
                profile.save()
                messages.success(request, "Phone Number successfully changed.")
            except:
                messages.error(request, "Phone Number change failed.")

        if country:
            try:
                profile.country = country
                profile.save()
                messages.success(request, "Country successfully changed.")
            except:
                messages.error(request, "Country change failed.")

        if city:
            try:
                profile.city = city
                profile.save()
                messages.success(request, "City successfully changed.")
            except:
                messages.error(request, "City change failed.")

        if address:
            try:
                profile.address = address
                profile.save()
                messages.success(request, "Address successfully changed.")
            except:
                messages.error(request, "Address change failed.")

        if website:
            try:
                profile.website = website
                profile.save()
                messages.success(request, "Website successfully changed.")
            except:
                messages.error(request, "Website change failed.")
        try:
            user.save()
        except:
            messages.error(
                request, "There was an error changing the data, please try again.")
        try:
            profile.save()
        except:
            messages.error(
                request, "There was an error changing the data, please try again.")

        return render(request, 'app/profile.html', {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_numer': profile.phone_numer,
            'country': profile.country,
            'city': profile.city,
            'address': profile.address,
            'website': profile.website,

        })


@login_required
def settings_edit(request):
    if request.POST:
        pass
