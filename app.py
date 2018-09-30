import os
import imp
from app import app

if __name__ == '__main__':
    app = imp.load_source('APIfirebase','app/APIfirebase')
    app.run()

def application(environ, start_response):
    start_response('200 OK', [('APIfirebase','app/APIfirebase')])
