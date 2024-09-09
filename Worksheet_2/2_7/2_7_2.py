start=600
end=800

for n in range(start, end+1):
    
    prime=True

    for i in range (2,n):
            if n%i==0:
                prime=False
                break
    
    if prime:
        print(n)

