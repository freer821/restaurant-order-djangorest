from .settings_comm import *

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['dk.ubonex.eu']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'whs_db',
        'USER': 'root',
        'PASSWORD': 'qwer1234@',
        'HOST': 'ub-mariadb',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
           'init_command': 'SET default_storage_engine=INNODB',
        }
    }
}