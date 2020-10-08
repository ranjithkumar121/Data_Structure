def search(arr,n,x):
    for i in range(0,n):
        if(arr[i] == x):
            return i
    return -1

arr = [1,2,6,3,7,8]
x = 1
n = len(arr)
result = search(arr,n,x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index ",result)


