from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # import messages
from django.contrib.auth.models import User
# Create your views here.

from payment.models import Product, StripeCustomer
from accounts.models import Profile, tests
from allauth.account.forms import ChangePasswordForm
from .search import return_articals
import stripe
from django.conf import settings as setting
from datetime import datetime



def main(request):
    stripe_list = Product.objects.all()
    try:
        test = tests.objects.get(user_id=request.user.id)
        test_acc = test.test_acc
    except:
        test_acc = 0

    return {
        'articals':return_articals,
        'product_list': stripe_list,
        'test_acc':test_acc
    }

def middleware_verified(request):
    if request.user.is_authenticated:
        if request.user.emailaddress_set.get().verified:
            return True
        else:
            return False 
        
def middleware_subscribe(request):
    
    try:
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = setting.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        # product = stripe.Product.retrieve(subscription.plan.product)

        # start_timestamp = subscription['current_period_start']
        # end_timestamp = subscription['current_period_end']
        # start_time = datetime.fromtimestamp(start_timestamp)
        # end_time = datetime.fromtimestamp(end_timestamp)

        # subscription['current_period_start'] = start_time
        # subscription['current_period_end'] = end_time
        return True
    except:
        return False

    

    # # return JsonResponse({
    # #     'subscription': subscription,
    # #     'product': product,
    # # })
    # return render(request, 'index.html', {
    #     'subscription': subscription,
    #     'product': product,
    # }) 

def middleware_profiles(request):
    try:
        tests.objects.get(user_id=request.user.id)

        return True
    except:
        return False

@login_required
def home(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc'],

        })
    
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    
    elif not middleware_profiles(request):
        return redirect('accounts')
    
    return render(request, 'app/index.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })


@login_required
def notifications(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    elif not middleware_profiles(request):
        return redirect('accounts')

    

    return render(request, 'app/notifications.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })

@login_required
def reviews(request):

    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })

    elif not middleware_profiles(request):
        return redirect('accounts')

    return render(request, 'app/reviews.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })




@login_required
def settings(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    elif not middleware_profiles(request):
        return redirect('accounts')
    

    return render(request, 'app/settings.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    # return render(request, 'app/index.html')


@login_required
def profile(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })


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
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    # return render(request, 'app/index.html')

@login_required
def profile_edit_page(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })

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
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })

@login_required
def plans(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    elif not middleware_profiles(request):
        return redirect('accounts')

    return render(request, 'app/plans.html', {
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    # return render(request, 'app/index.html')


@login_required
def accounts(request):

    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    
    try:
        test = tests.objects.get(user_id=request.user.id)
        test_acc = test.test_acc
    except:
        test_acc = 0

    if request.POST:
        try:
            test = tests.objects.get(user_id=request.user.id)
        except:
            user = User.objects.get(id=request.user.id)
            tests.objects.create( user=user)
            test = tests.objects.get(user_id=request.user.id)
       
        test.test_acc = 1
        test_acc = tests.test_acc
        test.save()

    return render(request, 'app/accounts.html', {
        'product_list': factory['product_list'] ,
        'articals': factory['articals'],
        'test_acc':test_acc,
    })


@login_required
def profile_edit(request):
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    

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
    factory = main(request)
    if not middleware_verified(request):
        return render(request, 'app/verified.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
    })
    elif not middleware_subscribe(request):
        return render(request, 'app/plan.html',{
        'product_list': factory['product_list'],
        'articals': factory['articals'],
        'test_acc': factory['test_acc']
        })
    elif not middleware_profiles(request):
        return redirect('accounts')

    if request.POST:
        pass
