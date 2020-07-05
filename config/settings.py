import os

ENV = os.environ.get('WHS_ENV')

if ENV == 'prod':
    print('starting prod environment.....')
    from .settings_prod import *
else:
    print('starting dev environment.....')
    from .settings_dev import *