def difference_from_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n

number = int(input("Enter a number: "))
result = difference_from_17(number)
print("The result is:", result)