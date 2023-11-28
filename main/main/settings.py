"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from smart_media.settings import *
from lotus.settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w(dq**jp--cf9co20e8b0adbmf=2v1x#3l56vr$pq@%!!h%x)p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['gmb-lb-146338110.eu-west-2.elb.amazonaws.com']
ALLOWED_HOSTS = ['*']

# Application definition
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
INSTALLED_APPS = [
    # blog
    "dal",
    "dal_select2",

    # admin theme
    "unfold",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'accounts',
    'payment',
    'app',

    # The following apps are required:
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',

    # blog
    "sorl.thumbnail",
    "smart_media",
    "ckeditor",
    "ckeditor_uploader",
    "taggit",
    "lotus",

    # theme
    # 'tailwind',
    # 'theme',
]
# TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",

    # blog
    "django.middleware.locale.LocaleMiddleware",
]


#  blog
LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", "English"),
)
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# This ensures you have all toolbar icons
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates", BASE_DIR / "static"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "google",
        "USER": "admin123",
        "PASSWORD": "admin123",
        "HOST": "gmb-main.cxri5qmltvjw.eu-west-2.rds.amazonaws.com",
        "PORT": "3306",
    }
}
CSRF_TRUSTED_ORIGINS = ['https://ziko.ai', 'https://www.ziko.ai']

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# STATIC_URL = 'static/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media', )
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

ACCOUNT_EMAIL_REQUIRED = True  # new

ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_LOGOUT_REDIRECT_URL = 'https://www.ziko.ai/'

ACCOUNT_EMAIL_VERIFICATION = 'optional'  # mandatory optional

SOCIALACCOUNT_AUTO_SIGNUP = True

SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            'client_id': '987428623868-mhetbn08b10o9qignhm2dt5i0vdto04t.apps.googleusercontent.com',
            'secret': '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',
            "key": ""
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        'OAUTH_PKCE_ENABLED': True,
        'EMAIL_AUTHENTICATION': True
    }
}


SOCIALACCOUNT_FORMS = {
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'accounts.forms.MyCustomSocialSignupForm',
}

ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm',
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.smtp2go.com'
EMAIL_HOST_USER = 'ziko.ai'
EMAIL_HOST_PASSWORD = "eAGmmV24XXxQiGBN"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Ziko Ai Support <support@ziko.ai>"

# test
# STRIPE_PUBLISHABLE_KEY = 'pk_test_51MQdxFJTQfFPcbL73Est7Xj7YaIU1WskNRGRkB9wIWjfT3kac90JpPd52orxov0EGKxZGmirY1Cd1iu5DpGkqmWA0063hdAQUd'
# STRIPE_SECRET_KEY = 'sk_test_51MQdxFJTQfFPcbL7ta7i4KQKW9hneN03pKLGEPWM0ire1UppxL96mZLeuEuLAWyhtqiOirGWF9n0I0txFShZ6TCu00dhtrr89F'


STRIPE_PUBLISHABLE_KEY = 'pk_live_51MQdxFJTQfFPcbL7perO2kRJn906Ol0n56DgKzJwrBmq75tGPcXrVVtLJQGBJrSnaCm93vonAJXBotRNnEczdOuk00MreOVa3Y'
STRIPE_SECRET_KEY = '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'

STRIPE_ENDPOINT_SECRET = 'whsec_xgUzgbB7V0YszaKMsGS2nIAYX6zWl3zf'
DOMAIN_URL = 'https://www.ziko.ai/'
