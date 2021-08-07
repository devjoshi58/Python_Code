#Convert dictionary to json
import json

person = {"name":"John","age":30,"city":"New York","hasChildren": False,"titles":['Programmer','Manager']}

personJson = json.dumps(person,indent=4,sort_keys=True) #Serialization

print(personJson)
print(type(personJson))

#Load the file to a file

with open('person.json','w') as f:
    #f.write(personJson)
    json.dump(person,f,indent=4) 


#Convert json back to python dictionary object which is called deserialization

person_dict = json.loads(personJson)
print(person_dict)
print(type(person_dict))


#Read from json file

with open('person.json','r') as file:
    person = json.load(file)
    print(type(person))
