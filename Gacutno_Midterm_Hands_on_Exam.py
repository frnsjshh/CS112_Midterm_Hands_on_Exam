import random
x = random.randint(1, 99)
y = random.randint(1, 99)
uservalue = eval(input(f"What is {x} + {y}?"))
check = x + y
if check == uservalue:
    print("Your answer is correct!")
else:
    print(f"Your answer {uservalue} is incorrect! The correct answer is {check}.")

