import os
import imp
   
def application(environ, start_response):
    start_response('200 OK', [('APIfirebase','app/APIfirebase.py')])
