def leftrotate(arr,d):
    if d==0:
        return 0
    n=len(arr)
    reversearray(arr,0,d-1)
    reversearray(arr,d,n-1)
    reversearray(arr,0,n-1)

def reversearray(arr,start,end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr [end]
        arr[end] = temp
        start +=1
        end -=1

def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i],end = ' ')


arr = [1,2,3,4,5,6,7]
n = len(arr)
d = 3
leftrotate(arr,d)
printArray(arr)
