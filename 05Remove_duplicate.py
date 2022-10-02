'''Write a program to remove all duplicates from a list '''
list1 = [1,2,2,3]
# l = set(list1) #set not contain any duplicate value 
# m = list(l)
# print(m)
i = 0
while(i < len(list1)):
    num = list1[i]
    for j in range(i+1,len(list1)-1):
        val = list1[j]
        if val == num:
            list1.pop(j)
    i = i + 1
print(list1)