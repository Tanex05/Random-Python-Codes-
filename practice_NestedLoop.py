#for x in range(4):
#    for y in range(3):
#        print(f"{x}, {y}")

numbers = [2, 2, 2, 2, 5]

for x in numbers:
    print("*" * x)
    
print("-------------------")   

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)