data = [9,7,5,3,1,2,4,6,8,10]
def bubblesort(array):
    for i in range(len(array)): #travesersing the whole array
        for j in range(0, len(array)-i-1):  #comparision

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print("Array Before sorting:")
print(data)

print("Array after sorting:")
k = bubblesort(data)
print(k)
