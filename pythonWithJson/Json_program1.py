import json

json_example = """{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}"""

menu = json.loads(json_example) #json string to python object using loads

print(menu)

for value in menu['menu']['popup']['menuitem']:
    #if value == 'popup':
    del(value)

back_to_json = json.dumps(menu, indent = 2,sort_keys=True) #json object to string

print(type(back_to_json))
print(back_to_json)
