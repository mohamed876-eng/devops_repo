import sys

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python calculatrice.py <operation> <a> <b>")
        sys.exit(1)

    operation = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if operation == "addition":
        result = addition(a, b)

    elif operation == "soustraction":
        result = soustraction(a, b)

    elif operation == "multiplication":
        result = multiplication(a, b)

    else:
        print("Opération inconnue:", operation)
        sys.exit(1)

    print("Résultat:", result)
