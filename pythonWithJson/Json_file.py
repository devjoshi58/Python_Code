import json

with open('json_sample_file.json','r') as j:
    out = json.load(j) #load used for reading json file


for state in out['states']:
    del(state['area_codes'])

#writing back to file, hence have to conver it back to json

with open('json_after_Deletion.json','w') as d:
    json.dump(out,d,indent=2)




