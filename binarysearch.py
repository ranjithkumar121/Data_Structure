def binarysearch(arr,l,r,x):
    if r >= 1:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr,l,mid-1,x)
        else:
            return binarysearch(arr,mid+1,r,x)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 6
n = len(arr)
result = binarysearch(arr,0,n-1,x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index ",result)