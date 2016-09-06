import random
arr = [random.randint(0,10000) for r in xrange(100)]

def bubbleSort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr
print bubbleSort(arr)
