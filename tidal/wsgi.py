#/usr/bin/python3
# -*- coding: utf-8 -*-


import os
from django.core.wsgi import get_wsgi_application


# =====================================================================================================================
# execute part
# =====================================================================================================================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tidal.settings")
application = get_wsgi_application()