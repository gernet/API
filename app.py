import os
import imp

if __name__ == '__main__':
    app = imp.load_source('APIfirebase','api/APIfirebase.py')
    app2 = imp.load_source('realace2018-firebase-adminsdk-r7gk1-121be5edaf.json','api/realace2018-firebase-adminsdk-r7gk1-121be5edaf.json')
    
#def application(environ, start_response):
#    start_response('200 OK', [('APIfirebase','app/APIfirebase.py')])
