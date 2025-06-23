# 5} itertools

#itertools is a set of helpful functions for looping
#part of the python standard python library

import itertools
import time

fruits = ['apple', 'orange', 'pear' ,'pineapple', 'durazno']

for a,b in itertools.pairwise(fruits):
    print(a,b)


print()
print()

b = 0
for a in itertools.cycle(['apple','orange']):
    print(a)
    b+=1
    print(b)

    time.sleep(0.5)
    if b == 10:
        break


#you can find the rest of itertools in the following directory:

print(dir(itertools))




    