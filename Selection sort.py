data = [9,7,5,3,1,2,4,6,8,10]

def selectionsort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i] , array[min_index] = array[min_index] , array[i]

print('List before sorting')
print(data)
selectionsort(data)
print('list after selection sorting')
print(data)