list1 = [1,4,1,5,6]
list2 = [2,1,5,6,3]
com = []

for i in range(len(list1)):
    for j in range(len(list2)):
        if(list1[i] == list2[j]):
            com.append(list1[i])


print(com)