D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

#Part 1
D[8] = 8.8
print("After adding new entry:", D)

#Part 2
D.pop(2, None)  
print("After removing key 2:", D)

#Part 3
key = 6
if key in D:
    print(f"Key {key} is present in the dictionary.")
else:
    print(f"Key {key} is not present in the dictionary.")

#Part 4
print("Number of elements in the dictionary:", len(D))

#Part 5
print("Sum of all values in the dictionary:", sum(D.values()))

#Part 6
D[3] = 7.1
print("After updating the value of key 3:", D)

#Part 7
D.clear()
print("After clearing the dictionary:", D)