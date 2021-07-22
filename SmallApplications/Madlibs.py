#Create a string with user inputs

#A few ways to concatenate string

adj = 'varun'
print("hey how are you "+adj)
print("hey how are you {}".format(adj))
print(f"hey how are you {adj}")

#madlibs

character1 = input("Your favorite avenger: ")
character2 = input("Deadly villian: ")
situation = input("situation: ")
result = input("what was the result: ")

madlib = f"There was a fight between {character1} and {character2} on the planet vormir \
because of {situation} and that led to {result}"

print(madlib)