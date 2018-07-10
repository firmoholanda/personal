import json, requests
    

r = requests.get(url='https://shiftstestapi.firebaseio.com/locations.json')
data = json.loads(r.content.decode())

print(data)
#print(type(data))


