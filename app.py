import os
import imp

if __name__ == '__main__':
    app = imp.load_source('APIfirebase','app/APIfirebase')

    
def application(environ, start_response):
    start_response('200 OK', [('APIfirebase','app/APIfirebase')])
