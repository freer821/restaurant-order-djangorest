import os

ENV = os.environ.get('WHS_ENV')

if ENV == 'prod':
    print('starting prod environment.....')
    #TODO
else:
    print('starting dev environment.....')
    from .settings_dev import *