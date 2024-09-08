input=input("Enter a sequence of comma-separated numbers: ")

numberstr=input.split(',')

list=[int(num) for num in numberstr]

tuple=tuple(list)

print("List:", list)
print("Tuple:", tuple)