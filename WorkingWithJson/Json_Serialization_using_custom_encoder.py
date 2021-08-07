import json

class user:

    def __init__(self,name,age):
        self.name= name
        self.age= age

userObj = user('max',34)

#Need custom function to make userObj serializable

def encode_user(o):
    if isinstance(o,user):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError


person = json.dumps(userObj,default=encode_user) #encode a custom object using the default argument
print(person)