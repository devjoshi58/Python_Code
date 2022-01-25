from datetime import datetime

def time_delta(t1,t2):

    
    #Sample Input
    """Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000 
    #Day dd Mon yyyy hh:mm:ss +xxxx
    """
    fmt = '%a %d %b %Y %H:%M:%S %z'

    
    delta = int(abs((datetime.strptime(t1,fmt))-(datetime.strptime(t2,fmt))).total_seconds())
    print(delta)

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

time_delta(t1,t2)