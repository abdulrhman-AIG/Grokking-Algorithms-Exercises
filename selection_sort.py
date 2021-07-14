def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

            smallest_index = i
    print(arr)
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))#stoooooooooooopppppppppp
        # print(newArr)
    return newArr


selectionSort([5, 3, 6, 2, 10])
