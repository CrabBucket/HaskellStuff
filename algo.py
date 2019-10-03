import math
import time
import random


def linearsearch(list,key):
    for maybe in list:
        if key == maybe:
            return True
    return False


def binarysearchI(list,key):
    start =0;
    end = len(list)-1
    middle = math.floor((end - start) / 2)
    while(start + 1 != end):
        if(start != end) : break
        elem = list[middle]
        if key > elem:
            start = middle
            middle = math.floor(middle + ((end-start)/2))
        elif key < elem:
            end = middle
            middle = math.floor(middle - ((end - start) / 2))
        else:
            return True
    return False



def binarysearchR(list, key):
    length = len(list)
    middle = list[math.floor(length/2)]
    if length == 1:
        return key == list[0]
        
    if key<middle:
        return binarysearchR(list[slice(math.floor(length/2))],key)
    elif key > middle:
        return binarysearchR(list[slice(math.floor(length/2),length)],key)
    else:
        return key == list[math.floor(length/2)]


list = sorted([random.randrange(-1000,1000) for i in range(int(input("Input size:")))])
randkeys = [random.randrange(-1000,1000) for i in range(int(input("Average Over:")))]
print("Linear Search:")
start = time.clock()
time.sleep(1)
for i in range(len(randkeys)):
    linearsearch(list, randkeys[i])

end1 = time.clock()
print("{:.10f} seconds".format((end1 / float(len(randkeys)))))

print("\n BinarySearch:")

for i in range(len(randkeys)):
    binarysearchI(list, randkeys[i])

end2 = time.clock()
print("{:.10f} seconds".format(((end2 - end1) / float(len(randkeys)))))