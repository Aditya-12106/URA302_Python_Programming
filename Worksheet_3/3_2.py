def is_within_range(number):
    if 100 <= number <= 1000 or number == 2000:
        return True
    else:
        return False
    
number = int(input("Enter a number: "))
if is_within_range(number):
    print(f"The number {number} is within the range 100 to 1000 or is equal to 2000.")
else:
    print(f"The number {number} is not within the range 100 to 1000 or equal to 2000.")    