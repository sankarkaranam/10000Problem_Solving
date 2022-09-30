import time
print("which table you want ?")
time.sleep(0.9)
num = int(input("Enter number here : "))
for i in range(1,11):
    time.sleep(0.5)
    print(f"{num} x {i} = {num*i}")