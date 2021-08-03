#Create your own exception

class ValueToHighError(Exception):
    pass

class ValueToSmallError(Exception):
    def __init__(self,messsage,value):
        self.message = messsage
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueToHighError("value too high")
    
    elif x<5:
        raise ValueToSmallError('VALUE TOO LOW',x)


try:
    test_value(2)
except ValueToHighError as e:
    print(e) 
except ValueToSmallError as e:
    print(e.value,e.message)
