temperature = 30

if temperature > 30:
    print("it's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")

print()
   
name = "Montano"
length = len(name)
if length < 3:
    print("name must be at least 3 Characters")
elif length > 50:
    print("name has a maximum of 50 Characters")
else:
    print("name looks good!")