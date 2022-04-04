"""
WSGI config for contactbook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

this_file = "venv/bin/activate_this.py"
exec(open(this_file).read(), {'__file__': this_file})

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactbook.contactbook.settings')

application = get_wsgi_application()
