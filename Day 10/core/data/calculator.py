def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    # ovaj blok koda izvrsi samo ako je calculator prvi (script)
    varA = input()
    varB = input()

    print(f"I want to saberi = {add(varA, varB)}")

    # end = ovaj blok koda izvrsi samo ako je calculator prvi (script)
