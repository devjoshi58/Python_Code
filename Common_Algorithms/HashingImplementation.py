#Hashing
#This doesnt take care of collisions

class basicHashTable():

    def __init__(self,max_hash_table_size):

        self.max_size = max_hash_table_size
        self.data_list = [None]*self.max_size
    
    def insert(self,key,value):

        idx = getIndex(self.data_list,key)

        self.data_list[idx]=(key,value)

    def find(self,key):

        idx = getIndex(self.data_list,key)

        if idx == None:
            return None
        else:
            key,value = self.data_list[idx]
        
        return (key,value)

    def update(self,key,new_value):

        idx = getIndex(self.data_list,key)

        self.data_list[idx] = (key,new_value)

    def extractAllKeys(self):

        list_of_keys = [kv[0] for kv in self.data_list if kv is not None]
        print(list_of_keys)

def getIndex(data_list,a_string):
    result = 0
    a_integer = 0
    for a_character in a_string:

        a_integer = ord(a_character) #Returns a number when applied on a string
        result+= a_integer
    
    # take the remainder of result with length of datalist

    idx = result% len(data_list)
    return(idx)


if __name__ == "__main__":

    data_list = [None]*4096
    idx =getIndex(data_list,"Varun")
    data_list[idx]=("Varun",'813')
    print(idx)
    data_list[idx]=("nurav",'813')
    
    print(idx)
    print(data_list[idx][0]) 

    obj1 = basicHashTable(50)
    obj1.insert('varun','8139986828')
    obj1.insert('joshi','816828')
    obj1.insert('nurav','81396828')

    res_key,res_value = obj1.find('varun')
    print(res_key,res_value)

    obj1.update('varun','00')
    res_key,res_value = obj1.find('varun')
    print(res_key,res_value)
    obj1.extractAllKeys()