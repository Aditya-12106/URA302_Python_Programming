S1= {10, 20, 30, 40, 50, 60}
S2= {40, 50, 60, 70, 80, 90}

#Part 1
S1.add(55)
S1.add(66)
print("After adding 55 and 66 to S1:", S1)

#Part 2
S1.remove(10)
S1.remove(30)
print("After removing 10 and 30 from S1:", S1)

#Part 3
if 40 in S1:
    print("40 is present in S1.")
else:
    print("40 is not present in S1.")

#Part 4
union_set = S1.union(S2)
print("Union of S1 and S2:", union_set)

#Part 5
intersection_set = S1.intersection(S2)
print("Intersection of S1 and S2:", intersection_set)

#Part 6
difference_set = S1.difference(S2)
print("Difference S1 - S2:", difference_set)