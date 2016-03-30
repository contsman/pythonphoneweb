# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from web import application

httpd = make_server('127.0.0.1',5555,application)
print('Serving HTTP on port 5555....')
httpd.serve_forever()
