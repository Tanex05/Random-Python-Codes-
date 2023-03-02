matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(matrix)

for row in matrix:
    for item in row:
        print(item)

test = [1,51234,30,4,5]
test.append(20)
print(test)
test.insert(0,100)
print(test)
test.remove(100)
print(test)
test.sort()
print(test)
test.pop()
print(test)
test.clear()
print(test)