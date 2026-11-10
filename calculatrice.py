import sys

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

if __name__ == "__main__":
     operation = sys.argv[1]
    a = float(sys.argv[2])
    b  = float(sys.argv[3])
if operation == "addition":
    print(addition(a, b))
elif operation == "soustraction":
     print(soustraction(a, b))
elif operation == "multiplication":
     print(multiplication(a, b))
else:
    print("Opération inconnue :", operation)