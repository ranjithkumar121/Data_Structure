def displaysublist(list):
    temp = [[]]
    for i in range(len(list)+1):
        for j in range(i+1,len(list)+1):
            sublist = list[i:j]
            temp.append(sublist)
    return temp


list = [1,2,3]
print("sublist is ",displaysublist(list))
