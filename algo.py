import math
import time
import random


def linearsearch(list,key):
    for maybe in list:
        
        if key == maybe:
            return True
    return False


def binarysearchI(list,key):
    start =0
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
start = time.time_ns() / 10**9

for i in range(len(randkeys)):
    linearsearch(list, randkeys[i])

end1 = time.time_ns() / 10**9

print("{:.10f} seconds".format(((end1-start) / float(len(randkeys)))))

print("\nBinarySearch:")

for i in range(len(randkeys)):
    binarysearchI(list, randkeys[i])

end2 = time.time_ns() / 10**9
print("{:.10f} seconds".format(((end2 - end1) / float(len(randkeys)))))

linearsearch(list, 5000)

end3 = time.time_ns() / 10**9
print("Worstcase for linear search: {:.10f} seconds".format(((end3-end2) / float(len(randkeys)))))

binarysearchI(list, 5000)

end4 = time.time_ns() / 10**9
print("Worstcase for binary search: {:.10f} seconds".format(((end4 - end3) / float(len(randkeys)))))

#For binary search: T(n) = T(n/2) + 5,  I think 5 is pretty fair looking at my code
#I counted 3 conditionals that must be evaluated every loop, and in the two most common
#IE the conditionals that get branched to when splitting the array I have two lines of code in each
#To control the start and end indicies within my array and also to recalculate the midpoint with the new
#Section of my array.
# Calculating T(N):  where T(N) = T(n/2) + 5 worstcase you get 5log(n) so to get the time it takes to run one line
#We can just do TotalTime/(Total Lines of Code) in the case of the worscase total lines of code is 5log(n)
#So we just do the time it takes to run the code / 5log(10^5) so our code to calculate that looks like:

linetimeb = (end4 - end3) / (math.log(len(list),2))
linetimel = (end3-end2) / (len(list))

print("Time to run 1 line of code as calculated from binary search: "+str(linetimeb))
print("Time to run 1 line of code as calculated from linear search: "+str(linetimel))

