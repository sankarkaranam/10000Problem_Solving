'''write a program that creates a list of 10 random integers. Then create two lists ODD and EVEN list'''
import random
num_list = []
for i in range(10):
    val = random.randint(1,100)
    num_list.append(val)
print("Origianl List : ",num_list)
even_list = []
odd_list = []
# for j in num_list:
#     if(j % 2 == 0):
#         even_list.append(j)
#     else:
#         odd_list.append(j)

# this is another logic 
for i in range(len(num_list)):
    if(num_list[i] % 2 == 0):
        even_list.append(num_list[i])
    else:
        odd_list.append(num_list[i])
print("Even List : ",even_list)
print("Odd List : ",odd_list)
