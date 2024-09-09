depth = 3
rows = 4
columns = 6

array_3d = [[[ '*' for _ in range(columns)] for _ in range(rows)] for _ in range(depth)]

for layer in array_3d:
    for row in layer:
        print(' '.join(row))
    print()