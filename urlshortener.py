import random
import json
import redis
import string
import bottle
from bottle import run, route, request, response, post, redirect
from redis import Redis

redis = Redis()

#generate 6 digit alpha-numeric string
def alphanum_code():
	code = ''
	for i in range(6):
		code += random.choice(string.lowercase + string.uppercase + string.digits)
	return code

# POST /shorten_url endpoint with json payload
@route('/shorten_url', method='POST')
def shorten_url():
	params = request.json
	custom_short_code = params['custom_short_code']
	long_url = params['long_url']
	if (not long_url):
		return 'Error: URL not specified'
	if (not custom_short_code):
		custom_short_code = alphanum_code()
	if redis.get(custom_short_code) is not None:
		return json.dumps(
            {'success' : 'false',
             'short_code': custom_short_code
             },
            indent=4)
	else:
	    redis.set(custom_short_code, long_url)
	return json.dumps(
        {'success' : 'true',
         'short_code': custom_short_code 
         },
        indent=4)
		
	
	

# redirect /{custom_short_code} endpoint to a long url
@route('/<custom_short_code>')
def redirect(custom_short_code):
	long_url = redis.get(custom_short_code)
	if  long_url is not None:
	    bottle.redirect(long_url, 301)
	else:
		return json.dumps(
            {'success' : 'false',
             'short_code': custom_short_code
             },
            indent=4)


if __name__ == '__main__':        
    # To run the server, type-in $ python server.py
    bottle.debug(True) # display traceback 
    run(host='localhost', port=8080, reloader=True) 



