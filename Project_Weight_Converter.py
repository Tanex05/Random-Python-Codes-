#question = int(input("Weight: "))
question = input("Weight: ")
Weight = int(question)

question2 = input("(L)bs or (K)g: ")


if question2.lower() == "l":
    print(f"You are {round(Weight / 0.45)} Pounds")
elif question2.lower() == "k":
    print(f"You are {round(Weight * 0.45)} Kilo")
else:
    print("Improper Input")