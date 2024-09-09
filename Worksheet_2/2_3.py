input = input("Enter numbers separated by spaces: ")
L = [int(x) for x in input.split()]
print(f"L={L}")
product=1;
for i in L:
    product*=i
print("Product of all items without using any inbuilt function is: ", product)    