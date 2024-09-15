def count_case_letters(s):
    count_upper = 0
    count_lower = 0
    
    for char in s:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    
    return count_upper, count_lower

string = input("Enter a string: ")
count_upper, count_lower = count_case_letters(string)
print(f"Uppercase letters: {count_upper}")
print(f"Lowercase letters: {count_lower}")