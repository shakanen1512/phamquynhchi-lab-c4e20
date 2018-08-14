x = int(input("x = "))
op = input("Operation(+,-,*,/) ")
y = int(input("y = "))

from eval import calc
result_2 = calc(x, y, op)

print("* " * 30)
print("{} {} {} = {}".format(x,op,y,result_2))
print("* " * 30)