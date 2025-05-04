from http.server import BaseHTTPRequestHandler
from maximos_invitation.wsgi import application
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maximos_invitation.settings')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from Python on Vercel!')

def vercel_handler(request):
    return Handler()