import httplib2
import json
import ast

# test urlshortener without specifying the long_url
def no_url_test():
    TESTDATA = {'long_url':'', 'custom_short_code':''}
    URL = 'http://localhost/shorten_url'
    jsondata = json.dumps(TESTDATA)
    h = httplib2.Http()
    resp, content = h.request(URL,
                          'POST',
                          jsondata,
                          headers={'Content-Type': 'application/json'})
    print resp
    print content
	
# test urlshortener without specifying the custom_short_code
def no_custom_short_code_test():
    TESTDATA = {'long_url':'http://www.google.com', 'custom_short_code':''}
    URL = 'http://localhost/shorten_url'
    jsondata = json.dumps(TESTDATA)
    h = httplib2.Http()
    resp, content = h.request(URL,
                          'POST',
                          jsondata,
                          headers={'Content-Type': 'application/json'})
    print resp
    print content
    return ast.literal_eval(content)
	
# test urlshortener by specifying the long_url and a custom_short_code
def has_custom_short_code_test():
    TESTDATA = {'long_url':'http://www.google.com', 'custom_short_code':'QWer12'}
    URL = 'http://localhost/shorten_url'
    jsondata = json.dumps(TESTDATA)
    h = httplib2.Http()
    resp, content = h.request(URL,
                          'POST',
                          jsondata,
                          headers={'Content-Type': 'application/json'})
    print resp
    print content
    return ast.literal_eval(content)
	
# test urlshortener to redirectto long_url using the short_code
def fetch_url_from_short_code_test(short_code):
    URL = 'http://localhost/'+short_code
    h = httplib2.Http()
    resp, content = h.request(URL,
                          'GET')
    print resp
    print content

if __name__ == '__main__':        
    # To test the server, run different test cases
    no_url_test() 
    short_code = no_custom_short_code_test()
    fetch_url_from_short_code_test(short_code['short_code'])
    short_code = has_custom_short_code_test()
    fetch_url_from_short_code_test(short_code['short_code'])
    

