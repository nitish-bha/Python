array = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(array)

x = 10
def binarysearch(array, x, low, high):
    while low<=high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
result = binarysearch(array,x,0,len(array)-1)
if result == -1:
    print("Element is not found in the array")
else:
    print(f"Element found at the index : {result}")