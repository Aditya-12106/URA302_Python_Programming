n=int(input("Enter a positive integer: "))

sum_of_squares=0

for i in range (1,n+1):
    sum_of_squares+= i**2

print(f"The sum of squares from 1^2 upto {n}^2 is: {sum_of_squares}")    