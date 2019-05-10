#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
tidal.settings

settings.py is the root configure file with tidal hunter engineering, and you can find some standards for
this file's coding in:

    * https://docs.djangoproject.com/en/1.8/topics/settings/
    * https://docs.djangoproject.com/en/1.8/ref/settings/
"""


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "this is a funny secret key for tidal hunter project as example"
DEBUG = True
ALLOWED_HOSTS = [
    '*'
]
ROOT_URLCONF = "tidal.urls"
WSGI_APPLICATION = "tidal.wsgi.application"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static").replace("\\", '/')
]
AUTH_USER_MODEL = "account.Employee"


# ===========================================================================================================
# main static cases config
# ===========================================================================================================
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
    "django.contrib.messages",
    "board",
    "account"
)

MIDDLEWARE_CLASSES = (
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ]
        }
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "tidal_hunter"
    }
}


# ===========================================================================================================
# other static cases config
# ===========================================================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = True