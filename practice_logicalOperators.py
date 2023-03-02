has_high_income = True
has_good_credit = True
has_crimanl_record = False

#both
#both statement should be true
if has_high_income and has_good_credit:
    print("You are eligible for a loan.")
else:
    print("You do not meet the requirement!")
    
print()

#at least one
#either statement should be true
if has_good_credit or has_high_income:
    print("Eligible for loan")
else:
    print("You are not Eligible for a loan")

print()   
#First statement must be true and second statement should always be false
#or argument will pass through the else statement
if has_high_income and not has_crimanl_record:
     print("Eligible for loan")
else:
    print("You are not Eligible for a loan")
