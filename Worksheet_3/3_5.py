def distinct_elements(lst):
    return list(set(lst))

input = input("Enter a list of elements separated by spaces: ").split()

try:
    List = list(map(int,input))
except ValueError:
    print("Non-integer values found. Keeping elements as strings.")

new_list = distinct_elements(List)

print("Original list:", List)
print("List with distinct elements:", new_list)