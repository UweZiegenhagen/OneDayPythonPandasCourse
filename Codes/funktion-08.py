def addthem(*args):
    result = 0
    for number in args:
        result += number
    return result


print(addthem(1, 2, 3, 4, 5))
