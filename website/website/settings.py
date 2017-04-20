"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g^ic@=ii08pq-g1ouh#*r=ic&ztb#m%60!4zdk9pyk2dvql_q%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['54.213.234.245', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings.apps.ListingsConfig',
    'storages',
    'rest_framework_swagger',
    'rest_framework',
    'customer',
    'vendor',
    'work_request',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mydb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

if 'S3_BUCKET_NAME' in os.environ:
    AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2034 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
    AWS_CLOUDFRONT_DOMAIN = os.environ['CLOUDFRONT_DOMAIN']
    AWS_ACCESS_KEY_ID = os.environ['S3_ACCESS_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET_KEY']

    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_HOST = 's3-us-west-2.amazonaws.com'

    # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
    # refers directly to STATIC_URL. So it's safest to always set it.

    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'website.custom_storages.StaticStorage'
    # STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    STATIC_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
    # STATIC_URL = '/static/'
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
        STATIC_PATH,
    )

    MEDIAFILES_LOCATION = 'media'
    # MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    MEDIA_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'website.custom_storages.MediaStorage'
    print "Using Aws  S3 config"
else:
    STATIC_URL = '/static/'

    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
        STATIC_PATH,
    )
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_static/')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'

REST_FRAMEWORK = {
    # Filters
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    # Test framework
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',

    # Auth
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.SessionAuthentication',
                                       'rest_framework.authentication.TokenAuthentication',),

    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25,

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
