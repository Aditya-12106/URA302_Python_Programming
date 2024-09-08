a,b,c=map(float,input("Enter the three angles of the desired triangle: ").split())

if a+b+c == 180:
    print("Yes, a triangle is possible.")

else:
    print("No, a triangle is not possible.")    