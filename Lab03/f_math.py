count = 0

while count < 5:
    from random import randint, choice
    x = randint(1, 10)
    y = randint(1, 10)
    calc_list = ["+", "-", "*", "/"]
    calc = choice(calc_list)
    error_list = [-1, 0, 0, 0, 1]
    error = choice(error_list)

    if calc == "+":
        display_result = x + y + error
    elif calc == "-":
        display_result = x - y + error
    elif calc == "*":
        display_result = x * y + error
    else:
        display_result = x / y + error

    print("* " * 30)
    print("{} {} {} = {}".format(x,calc,y,display_result))
    print("* " * 30)

    guess = input("Y/N? ").upper()
    if error == 0 and guess == "Y":
        print("Yay")
    if error == 0 and guess == "N":
        print("Wrong")
        break
    if error != 0 and guess == "Y":
        print("Wrong")
        break
    if error != 0 and guess == "N":
        print("Yay")

    count += 1