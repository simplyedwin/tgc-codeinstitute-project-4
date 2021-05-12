"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

UPLOADCARE = {
    'pub_key': os.environ.get('UPLOADCARE_PUBLIC_KEY'),
    'secret': os.environ.get('UPLOADCARE_SECRET_KEY')
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@8gj!oy$g-%!*_hh5j0s2+60ly6&t5w#qpacyhfg!^7+4jigh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','simplyedwin-tgc-proj4.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'pyuploadcare.dj',
    'crispy_forms',
    'products',
    'users',
    'checkout',
    'reviews',
    'cart'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# to login via email or username
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# to indicate whether email address is require when registering
ACCOUNT_EMAIL_REQUIRED = True
# to indicate whether email verification is needed from the user before they can sign in
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# to indicate whether user needs to provide the email address twice to prevent misspelling
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# to indicate the min length for username
ACCOUNT_USERNAME_MIN_LENGTH = 4
# the url for login
LOGIN_URL = '/accounts/login/'
# to direct to the page when login is successful
LOGIN_REDIRECT_URL = '/'

# instead of sending emails, just display them in the terminal for us to see
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# # simulate Django to send out emails
# TEST_EMAIL = os.environ.get("TEST_EMAIL")
# print(TEST_EMAIL)
# if TEST_EMAIL == 1:    
#     print("result")
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#     print(EMAIL_BACKEND)
# else:
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     EMAIL_USE_TLS = True
#     EMAIL_PORT = 587
#     EMAIL_HOST = "smtp.gmail.com"
#     EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
#     EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
#     DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_SUCCESS_URL = os.environ.get('STRIPE_SUCCESS_URL')
STRIPE_CANCEL_URL = os.environ.get('STRIPE_CANCEL_URL')
STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET')