from multiprocessing.reduction import duplicate
import re


def remove(duplicate):
    new_list = []
    for num in duplicate:
        if num not in new_list:
            new_list.append(num)
    return new_list

list1 = [1,2,3,4,2,3,5,6]
print(remove(list1))


# This is another method to remove elements
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))

#this is another method to remove the duplicate elements in the list 
input_list = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8]
mylist = list(dict.fromkeys(input_list))
print(mylist)

