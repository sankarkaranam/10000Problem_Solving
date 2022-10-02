num_list = []
for i in range(1,21):
    num_list.append(i)
print("Original List : ", num_list)
odd_list = []
for j in num_list:
    if(j % 2 != 0):
        odd_list.append(j)
print("Odd Numbers : ",odd_list)

#Short Method for print odd numbers
odd = [2*i+1 for i in range(20)]
print(odd)