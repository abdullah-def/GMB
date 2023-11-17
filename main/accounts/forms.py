from django import forms
from allauth import account
from allauth import socialaccount
from django.contrib.auth.hashers import make_password

class CustomSignupForm(account.forms.SignupForm):
    first_name = forms.CharField(max_length=25, label='first_name')
    last_name = forms.CharField(max_length=25, label='last_name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    
class MyCustomSocialSignupForm(account.forms.BaseSignupForm):

    password1 = account.forms.SetPasswordField(label=("Password"))
    password2 = account.forms.SetPasswordField(label=("Confirm Password"))

    def __init__(self, *args, **kwargs):
        self.sociallogin = kwargs.pop('sociallogin')
        user = self.sociallogin.user
        # TODO: Should become more generic, not listing
        # a few fixed properties.
        initial = {'email': account.utils.user_email(user) or '',
                   'username': account.utils.user_username(user) or '',
                   'first_name': account.utils.user_field(user, 'first_name') or '',
                   'last_name': account.utils.user_field(user, 'last_name') or ''}
        kwargs.update({
            'initial': initial,
            'email_required': kwargs.get('email_required',
                                         account.app_settings.EMAIL_REQUIRED)})
        super(MyCustomSocialSignupForm, self).__init__(*args, **kwargs)
    
    def save(self, request):
        adapter = socialaccount.adapter.get_adapter()
        user = adapter.save_user(request, self.sociallogin, form=self)
        self.custom_signup(request, user)
        return user


    def clean(self):
        super(MyCustomSocialSignupForm, self).clean()
        if "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                raise forms.ValidationError(_("You must type the same password"
                                              " each time."))

    def raise_duplicate_email_error(self):
        raise forms.ValidationError(
            _("An account already exists with this e-mail address."
              " Please sign in to that account first, then connect"
              " your %s account.")
            % self.sociallogin.account.get_provider().name)

    def custom_signup(self, request, user):
        password = self.cleaned_data['password1']
        user.password = make_password(password)
        user.save()
    