import random
x = random.randint(1, 99)
y = random.randint(1, 99)
uservalue = eval(input(f"What is {x} + {y}?" ))
check = x + y
if check == uservalue:
    print("Your answer is correct!")
else:
    print(f"Your answer {uservalue} is incorrect! The correct answer is {check}.")

a = random.randint(1, 99)
b = random.randint(1, 99)
userminus = eval(input(f"What is {a} - {b}?" ))
checkminus = x - y
if checkminus == userminus:
    print("Your answer is correct!")
else:
    print(f"Your answer {userminus} is incorrect! The correct answer is {checkminus}.")

c = random.randint(1, 99)
d = random.randint(1, 99)
uservalue2 = eval(input(f"What is {c} x {d}?" ))
check2 = x * y
if check2 == uservalue2:
    print("Your answer is correct!")
else:
    print(f"Your answer {uservalue2} is incorrect! The correct answer is {check2}.")


e = random.randint(1, 99)
f = random.randint(1, 99)
uservalue3 = eval(input(f"What is {c} / {d}?" ))
check3 = x / y
if check3 == uservalue3:
    print("Your answer is correct!")
else:
    print(f"Your answer {uservalue3} is incorrect! The correct answer is {check3}.")
