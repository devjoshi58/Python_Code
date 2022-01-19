from datetime import datetime
    
data = [
    {"id": 1, "period": "1/1/2000", "value": 13},
    {"id": 2, "period": "3/1/2021", "value": 52},
    {"id": 3, "period": "3/1/2019", "value": 43},
    {"id": 4, "period": "6/1/2016", "value": 27}
    #{"id": 5, "period": "Jan 2020", "value": 12312},
    #{"id": 6, "period": "Mar 2020", "value": 23423}
]

print(data[0]['period'])

new_list = sorted(data,key=lambda x :datetime.strptime(x['period'],'%m/%d/%Y'))
print(new_list)