from random import randint, choice
from eval import calc

def generate_quiz():
    x = randint(1, 10)
    y = randint(1, 10)
    op_list = ["+", "-", "*", "/"]
    op = choice(op_list)
    error_list = [-1, 0, 0, 0, 1]
    error = choice(error_list)

    if op == "+":
        result = x + y + error
    elif op == "-":
        result = x - y + error
    elif op == "*":
        result = x * y + error
    else:
        result = x / y + error

    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    true_result = calc(x, y, op)
    if true_result == result:
        return user_choice
    else:
        return not user_choice
    
