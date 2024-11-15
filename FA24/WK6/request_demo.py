import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.json())

post_r = requests.post('https://httpbin.org/post', data={'key': 'value', 'key2': 'value2'})
print(post_r.json())

get_args = {'q': 'Disenchant', 'e':'BRO'}
get_r = requests.get('https://pricing.grixisutils.site/search', params=get_args)
print(get_r.url)
