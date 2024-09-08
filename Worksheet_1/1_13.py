principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
years = int(input("Enter the number of years the money is invested: "))

rate=rate/100

amount=principal*(1+rate/times_compounded)**(times_compounded*years)

compound_interest=amount- principal

print(f"The compound interest is: {compound_interest:.2f}")