#definition
#argument
def calc(x, y, calc):

    if calc == "+":
        result = x + y
    elif calc == "-":
        result = x - y
    elif calc == "*":
        result = x * y
    elif calc == "/":
        result = x / y

    return result

#call
# big_result = calc(10, 15, "-")
# print(big_result)