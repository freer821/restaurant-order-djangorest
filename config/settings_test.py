from .settings_comm import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '192.168.178.78']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'whs_db',
        'USER': 'root',
        'PASSWORD': 'qwer1234@',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
           'init_command': 'SET default_storage_engine=INNODB',
        }
    }
}
