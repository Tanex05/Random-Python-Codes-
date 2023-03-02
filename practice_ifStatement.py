is_hot = False
is_cold = True

if  is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
    
print()

Cash = 100000    
has_good_credit = False

if has_good_credit:
    print(f"You are eligible for a 20% down")
    down_payment = Cash * 0.2
else:
    print(f"You are only eligible for a 10% down")
    down_payment = Cash * 0.1
print(f"Downpayment of {Cash}$ is {down_payment}$")