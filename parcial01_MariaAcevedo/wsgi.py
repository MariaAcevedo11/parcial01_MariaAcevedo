"""
WSGI config for parcial01_MariaAcevedo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parcial01_MariaAcevedo.settings")

application = get_wsgi_application()
