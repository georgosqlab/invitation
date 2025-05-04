from maximos_invitation.wsgi import application


def app(environ, start_response):
    # Special handling for static files if needed
    if environ["PATH_INFO"].startswith("/static/"):
        start_response("404 Not Found", [])
        return []

    # Pass all other requests to Django
    return application(environ, start_response)