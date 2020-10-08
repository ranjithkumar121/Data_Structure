def rotate(arr,n,d):
    for i in range(d):
        leftrotatebyone(arr,n)

def leftrotatebyone(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

arr = [1,2,3,4,5,6,7]
rotate(arr,7,2)
print(arr)


