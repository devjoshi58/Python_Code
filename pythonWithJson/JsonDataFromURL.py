import json
from textwrap import indent
from urllib.request import urlopen

with urlopen("http://api.plos.org/search?q=title:DNA") as response:

    source = response.read()

#print(type(source))

data = json.loads(source) # converting to python object dict

#print(type(data))

#print(json.dumps(data,indent=2))

print(len(data['response']['docs']))

for i in data['response']['docs']:
    print((i['journal'],i['publication_date']))