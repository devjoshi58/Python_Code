#Using secret library for tokens,password etc

import secrets

a = secrets.randbelow(10) #10 is the upper bound
print(a)

b = secrets.randbits(4) #4 bits
#1010
#highest possible number 1111 which is 15
print(b)