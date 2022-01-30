from datetime import datetime 
import os
"""
s= 'Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON'
s2='Jul 11 16:11:55:490 [139681125603136] dut: Device State: OFF'
l = s[:19]
l2=s2[:19]

#if l[-1]=='ON':
#    start = l[2]

#if l2[-1]=='OFF':
#    stop = l[2] 
logs_sample.txt
print((datetime.strptime(l,"%b %d %H:%M:%S:%f")-datetime.strptime(l2,"%b %d %H:%M:%S:%f")).total_seconds())
"""
#print(os.curdir())

def getevent():
    with open("/Users/varunjoshi/Documents/GitHub/Python_Code/logs_sample.txt","r") as f:

        for line in f:
            if 'dut: Device State:' in line:
                status = line.split()[-1]
                time = line[:19]
                yield (status,time) #get one item at a time

def extractTime():
    IsDeviceOn = False

    for value,time in getevent():

        if value=='ON' and IsDeviceOn==False:
            timeOn = time
            IsDeviceOn=True
        
        elif value=='OFF' and IsDeviceOn==True:
            timeOff = time
            IsDeviceOn = False
            diff = calculateTimeDifference(timeOn,timeOff)
            print(timeOn,timeOff,diff)


def calculateTimeDifference(timeOn,timeOff):

    difference = (datetime.strptime(timeOn,"%b %d %H:%M:%S:%f")-datetime.strptime(timeOff,"%b %d %H:%M:%S:%f")).total_seconds()
    return(difference)

if __name__ == "__main__":
    extractTime()
