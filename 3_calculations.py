def calculations(operator, first, second):
    result = None
    if operator == "multiply":
        result = first * second
    elif operator == "divide":
        result = int(first / second)
    elif operator == "add":
        result = first + second
    elif operator == "subtract":
        result = first - second
    return result


operator = input()
first = int(input())
second = int(input())

print(calculations(operator, first, second))
