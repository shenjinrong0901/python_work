'''
def add():
    s = 0
    for i in range(100):
        s += i+1
    print("Sum:", s)

def star():
    n = int(input("Please input number:"))
    for i in range(n):
        print("*" * i)

add()
star()
'''

import time
def sum0fN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end-start

for i in range(5):
    print("Sum is %d required %10.7f seconds"
          % sum0fN2(10000))
 

