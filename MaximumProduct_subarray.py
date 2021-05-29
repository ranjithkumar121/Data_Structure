def maximumSubarray(arr,n):
    result=arr[0]

    for i in range(n):
        mul=arr[i]

        for j in range(i+1,n):
            result=max(result,mul)
            mul=mul*arr[j]

        result=max(result,mul)
    return result
                   

arr=list(map(int,input().split()))
n=len(arr)
print(maximumSubarray(arr,n))
