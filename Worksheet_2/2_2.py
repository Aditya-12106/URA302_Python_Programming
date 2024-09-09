input = input("Enter numbers separated by spaces: ")
L = [int(x) for x in input.split()]
print(f"L={L}")
sum=0;
for i in L:
    sum+=i
print("Sum of all items without using any inbuilt function is: ", sum)    