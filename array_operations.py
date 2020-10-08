arr=[1,2,3,4,]

print("the new created array is :",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\r")

arr.append(5)
print("The appended array is :",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\r")

arr.insert(5,6)
print("The array after insertion is :",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\r")

arr.pop(2)
print("The array after popping is :",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\r")

arr.remove(1)
print("The array after removing is :",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\r")

arr.reverse()
print("The array after reversing is :",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")




