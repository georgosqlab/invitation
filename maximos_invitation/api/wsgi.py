from maximos_invitation.wsgi import application

def app(environ, start_response):
    path = environ["PATH_INFO"]
    if path.startswith("/static/"):
        # Let Vercel handle static files
        start_response("404 Not Found", [])
        return []
    return application(environ, start_response)