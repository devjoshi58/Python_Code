"""generator functions are a special kind of function that return a lazy iterator. These are objects
 that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory."""

 #Can be used to load and read a huge file

def csv_reader(file):
    for row in open(file,"r"):
        yield row #using yeild results in generator object


csv_gen = csv_reader("/Users/varunjoshi/Downloads/some_csv.txt")
count = 0
for row in csv_reader("/Users/varunjoshi/Downloads/some_csv.txt"): #Reads row one by one and doesnt load all the data into memory at once
    count+=1

print(count)

#Create function to generate infinite numbers

def infinitenumbers():
    num = 0
    while True:
        yield num
        num+=1

for i in infinitenumbers():
    print(i)