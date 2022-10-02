from traceback import print_tb


num_list = []
m = int(input("Enter the String of the range : "))
n = int(input("Enter the Ending of the range : "))
step = int(input("Enter the steps in the range : "))

for numbers in range(m,n,step):
    num_list.append(numbers)
print("Original List : ",num_list)
num_list.reverse()
print("Reverse List : ",num_list)