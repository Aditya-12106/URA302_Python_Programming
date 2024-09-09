input = map(int,input("Enter a list of numbers separated by spaces: ").split())

numbers = list(input)
print(f"Given list={numbers}")
print("Numbers divisible by 5: ")
for n in numbers:
    if n%5==0:
        print(n)