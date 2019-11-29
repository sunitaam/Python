from array import *

arr = array('i',[])
n = int(input("Enter size of array"))
print(n)

j=0
for i in range(n):
    i= int(input("Enter next element"))
    arr.append(i)

for j in range(n):
    print(arr[j])
    j=j+1
#arr = arr+5
print(arr)

s = int(input("Enter value to be searched"))
for e in arr:
    if e==s:
        print(e)
        break


