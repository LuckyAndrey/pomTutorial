import requests, time


payload = {'ts': time.time()}

r = requests.post('http://requestb.in/uaqgg3ua', data = payload)
print(r.status_code)
# print(r.content)
from requests_html import HTMLSession

session = HTMLSession()

ddd = session.get('https://mail.ru')
print(ddd.status_code)
# print('links ', ddd.html.links)

for i in ddd.html.links:
    try:
        r = requests.get(i)
        if r.status_code == 200:
            continue
            print(type(r.status_code), r.status_code , '  ', i)
            # print(i)
        else:
            print('broken link ', r.status_code, ' link  ', i)

    except:
        pass



'''

r = requests.get('http://swapi.co/api/')
print(r)
print(r.url)
# print(r.json()['name'])
d = (r.json())
# print(d)

dd = dict(d)
# print(dd)
for k,v in dd.items():
    print(k,' - ', v)

print(r.request)

'''