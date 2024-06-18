array = [3,6,4,1,8,9,7]
print(array)

x = 18
n = len(array)

def linearsearch(array,n,x):
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1
result = linearsearch(array,n,x)

if result == -1:
    print("Element is not found in the array")
else:
    print(f"Element found at the index : {result}")
