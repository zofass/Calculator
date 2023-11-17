first_value = int(input("Please enter first number: "))
action = input("Please enter action: ")
second_value = int(input("Please enter second number: "))


if action == ('+'):
    print(first_value + second_value)
elif action == ('-'):
    print(first_value - second_value)
elif action == ('*'):
    print(first_value * second_value)
elif action == ('/'):
    if second_value != 0:
        print(first_value / second_value)
    else: print("You can't divide by 0")








