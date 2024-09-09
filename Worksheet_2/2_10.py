number = int(input("Enter a number: "))

is_even = (number % 2 == 0)
is_odd = (number % 2 != 0)

if is_even:
    print(f"The number {number} is even.")
elif is_odd:
    print(f"The number {number} is odd.")
else:
    print("Something went wrong.")
