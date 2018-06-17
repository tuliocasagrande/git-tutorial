def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b."""
    if b == 0:
        return 'division by zero!'
    return a / b


if __name__ == '__main__':
    a = 2
    b = 3
    print(f'{a} * {b} == {multiply(a, b)}')
    print(f'{a} / {b} == {divide(a, b)}')
