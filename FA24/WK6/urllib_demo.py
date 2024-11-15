import urllib3
import http as http_module

http = urllib3.PoolManager()

def code_to_str(html_code):
    return http_module.HTTPStatus(html_code).phrase

resp = http.request('GET', 'http://gogle.com', redirect=True)
print(resp.status, code_to_str(resp.status))
#print(resp.data)

resp = http.request('GET', 'http://gogle.com', redirect=False)
print(resp.status, code_to_str(resp.status))
#print(resp.data)

# this will throw an error due to ssl cert issues! (maybe explain this)

#resp = http.request('GET', 'https://gogle.com', redirect=True)
#print(resp.data)
