#The below code creates an array named array1
from array import *
array1 = array('i', [10,20,30,40,50])
print(array1[2])
print(array1[4])

#inserting
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
    print(x)

#removing element

from array import *

array1 = array('i', [10,20,30,40,50])

array1.remove(40)

for x in array1:
    print(x)

#searching
from array import *

array1 = array('i', [10,20,30,40,50])

print (array1.index(40))

#Update operation
from array import *

array1 = array('i', [10,20,30,40,50])

array1[2] = 80

for x in array1:
    print(x)


