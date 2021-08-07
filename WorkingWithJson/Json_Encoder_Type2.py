import json
#import Json_Serialization_using_custom_encoder
from json import JSONEncoder

class user:

    def __init__(self,name,age):
        self.name= name
        self.age= age

userObj = user('max',34)
#Overrride the default method in the class JSONEncoder

class UserEncoder(JSONEncoder): #inheritance

    def default(self,o):
        if isinstance(o,user):
            return {'name':o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)

#userjson = UserEncoder().encode(userObj)
userjson = json.dumps(userObj,cls= UserEncoder) # same as above line 
print(type(userjson))

