def multiply(arr, multiple):
    for i in range(0,len(arr)):
        arr[i] *= multiple
    return arr

a = [2,4,10,16]
b = multiply(a, 5)
print b
