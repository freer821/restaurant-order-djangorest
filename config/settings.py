import os

ENV = os.environ.get('WHS_ENV')

if ENV == 'prod':
    print('starting prod environment.....')
    from .settings_prod import *
elif ENV == 'test':
    print('starting test environment.....')
    from .settings_test import *
else:
    print('starting dev environment.....')
    from .settings_dev import *