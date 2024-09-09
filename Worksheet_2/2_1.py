L=[11,12,13,14]

#Part 1
L.append(50)
L.append(60)
print("After adding 50 and 60:", L)

#Part 2
L.remove(11)
L.remove(13)
print("After removing 11 and 13:", L)

#Part 3
L.sort()
print("Sorted in ascending order:", L)

#Part 4
L.sort(reverse=True)
print("Sorted in descending order:", L)

#Part 5
a = 13
if a in L:
    print(f"{a} is in the list.")
else:
    print(f"{a} is not in the list.")

#Part 6
print("Number of elements in L:", len(L))    

#Part 7
print("Sum of all elements:", sum(L))

#Part 8
odd_sum=0;
for i in L:
    if i%2 !=0:
        odd_sum+=i
print("Sum of all odd elements: ", odd_sum)        

#Part 9
even_sum=0;
for i in L:
    if i%2 ==0:
        even_sum+=i
print("Sum of all even elements: ", even_sum)  

#Part 10
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

prime_sum = 0
for x in L:
    if is_prime(x):
        prime_sum+=x
print("Sum of all prime numbers:", prime_sum)

#Part 11
L.clear()
print("List after clearing all elements:", L)

#Part 12
del L