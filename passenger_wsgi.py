import sys, os
sys.path.append(os.getcwd())
INTERP = "/home/misterinterrupt/.virtualenvs/matthewdhowell/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

os.environ['DJANGO_SETTINGS_MODULE'] = "matthewdhowell.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()