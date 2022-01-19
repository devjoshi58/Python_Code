from datetime import datetime

ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08',
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
    '2019-02-07',
    '2019-02-08'
]

res=[]

ts.sort()
#print(ts)

#print(datetime.strptime(ts[0],'%Y-%m-%d')-datetime.strptime(ts[1],'%Y-%m-%d'))
i=0
while i < len(ts):
    l=[ts[i]]
    print(l)
    j=i+1
    while j<len(ts):
        if  datetime.strptime(ts[j],'%Y-%m-%d').month==datetime.strptime(ts[i],'%Y-%m-%d').month and datetime.strptime(ts[j],'%Y-%m-%d').day - datetime.strptime(ts[i],'%Y-%m-%d').day<7  :
            print(datetime.strptime(ts[j],'%Y-%m-%d').day - datetime.strptime(ts[i],'%Y-%m-%d').day)
            #print(ts[j])
            l.append(ts[j])
        else:
            break
        j=j+1
    res.append(l)
    i=j
#res.append([ts[len(ts)-1]])
print(res)

#rint(res.append(ts[i]))
