list1_input = map(int,input("Enter the first list of numbers separated by spaces: ").split())
list2_input = map(int,input("Enter the second list of numbers separated by spaces: ").split())

list1=list(list1_input)
list2=list(list2_input)

odd_numbers = [num for num in list1 if num % 2 != 0]
even_numbers = [num for num in list2 if num % 2 == 0]

new_list = odd_numbers + even_numbers

print("New list containing odd numbers from list1 and even numbers from list2= ", new_list)