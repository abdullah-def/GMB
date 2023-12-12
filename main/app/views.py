from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # import messages
from django.contrib.auth.models import User
# Create your views here.

from payment.models import Product, StripeCustomer
from accounts.models import Profile, test
from allauth.account.forms import ChangePasswordForm
from .search import return_articals

def main():
    stripe_list = Product.objects.all()
    return {
        'articals':return_articals,
        'product_list': stripe_list,
    }

@login_required
def home(request):

    factory = main()
    return render(request, 'app/index.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals']
    })


@login_required
def notifications(request):
    factory = main()
    return render(request, 'app/notifications.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals']
    })

@login_required
def reviews_list(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/reviews_list.html', {
        'product_list': stripe_list
    })

@login_required
def reviews_analysis(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/reviews_analysis.html', {
        'product_list': stripe_list
    })

@login_required
def business_details(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/business_details.html', {
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
    factory = main()
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    myform = ChangePasswordForm()
    return render(request, 'app/profile1.html', {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_numer': profile.phone_numer,
        'country': profile.country,
        'city': profile.city,
        'address': profile.address,
        'website': profile.website,
        'form': myform,
        'product_list': factory['product_list'],
        'articals': factory['articals']
    })
    # return render(request, 'app/index.html')

@login_required
def profile_edit_page(request):
    factory = main()
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user_id=request.user.id)
    myform = ChangePasswordForm()
    return render(request, 'app/profile_edit.html', {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_numer': profile.phone_numer,
        'country': profile.country,
        'city': profile.city,
        'address': profile.address,
        'website': profile.website,
        'form': myform,
        'product_list': factory['product_list'],
        'articals': factory['articals']
    })

@login_required
def plans(request):
    stripe_list = Product.objects.all()

    return render(request, 'app/plans.html', {
        'product_list': stripe_list
    })
    # return render(request, 'app/index.html')


@login_required
def accounts(request):
    factory = main()
    
    try:
        tests = test.objects.get(user_id=request.user.id)
        test_acc = tests.test_acc
    except:
        test_acc = 0

    if request.POST:
        try:
            tests = test.objects.get(user_id=request.user.id)
        except:
            user = User.objects.get(id=request.user.id)
            test.objects.create( user=user)
            tests = test.objects.get(user_id=request.user.id)
        tests.test_acc = 1
        test_acc = tests.test_acc
        tests.save()

    return render(request, 'app/accounts.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc':test_acc,
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
