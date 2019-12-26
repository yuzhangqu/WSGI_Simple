# -*- coding: utf-8 -*-
from webob import Response
from webob.dec import wsgify
from wsgiref.simple_server import make_server

@wsgify
def app(request):
    return Response('<h1>Hello World!</h1>')

with make_server('0.0.0.0', 8000, app) as httpd:
    httpd.serve_forever()
