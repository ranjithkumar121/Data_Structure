def leftArrayRotation(array,shift):
    for i in range(0,shift):
        temp=array[0]

        for j in range(0,len(array)-1):
            array[j] = array[j+1]

        array[j+1] = temp

    return array

array = [1,2,3,4,5]
shift = 2
rotatedArray = leftArrayRotation(array,shift)
print(rotatedArray)