from maximos_invitation.wsgi import application
from django.urls import set_script_prefix

def app(environ, start_response):
    # Set script prefix if needed
    set_script_prefix('/')
    return application(environ, start_response)