def arithmetic(x, y):
    a = x
    b = y
    a = (a * b) * b
    c = a - 5
    return c


if __name__ == "__main__":
    result = arithmetic(10, 0)
    print(result)
