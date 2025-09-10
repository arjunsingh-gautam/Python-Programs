l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1[0][2])
print(l1[2][1])

for row in l1:
    print(row)

for row in l1:
    for element in row:
        print(element,end=' ')
    print()