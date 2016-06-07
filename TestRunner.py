try:
    print(1/0)
except ArithmeticError as err:
    print(err)
