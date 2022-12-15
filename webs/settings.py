
from pathlib import Path
import os
from django.contrib.messages import constants as message_constants
import cloudinary
import cloudinary_storage
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '42037h6jqq=j&-r0ydft1@!bmz4*1mr*h#ay!=cyj#+m-wp868'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'miwebapp',
    'rutinasapp',
    'forms',
    'auntenti',
    'crispy_forms',
    'products',
    'cart',
    'orders',
    # 'markdown_deux',
    'cloudinary',
    'cloudinary_storage',
]


#paquetesproyecto


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'webs.urls'

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
                'cart.context_processor.cart_total_amount',
                'cart.context_processor.num_products',
            ],
        },
    },
]

WSGI_APPLICATION = 'webs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd2aplu6aab6o5e',
#         'USER':'cnsyrnjwbdgqzb',
#         'PASSWORD':'aad0d302e24fddae0bede216c17b31ab2aa13844820972d18a454e63d5511f91',
#         'HOST':'ec2-54-224-120-186.compute-1.amazonaws.com',
#         'DATABASE_PORT':'5432',
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'companyseller.ml@gmail.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
# STATIC_URL='/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
CRISPY_TEMPLATE_PACK = 'bootstrap4'
STATIC_FILES = (
    os.path.join(BASE_DIR,'static'),
)

MEDIA_URL='/media/'
#MEDIA_ROOT=os.path.join(BASE_DIR,'media')

MESSAGE_TAGS={
    message_constants.DEBUG:'debug',
    message_constants.INFO:'info',
    message_constants.SUCCESS:'success',
    message_constants.WARNING:'warning',
    message_constants.ERROR:'danger',
}
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'tolumaster',
    'API_KEY': '238229748389954',
    'API_SECRET': '64KwWcwxJ7OikMWHiTv7gUdE_5o',
}
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'tolumaster',
#     'API_KEY': '238229748389954',
#     'API_SECRET': '64KwWcwxJ7OikMWHiTv7gUdE_5o',
     
# }
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# # JAZZMIN_SETTINGS["show_ui_builder"] = True
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'mediafiles')
# MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'