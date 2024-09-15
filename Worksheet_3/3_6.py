def even_numbers(lst):
    
    even_list=[]

    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

input=map(int,input("Enter a list of numbers separated by spaces: ").split())
List=list(input)

even_list=even_numbers(List)

print("Even numbers in the list are: ")
for n in even_list:
    print(n)