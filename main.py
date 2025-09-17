from sum import add
from difference import subtract
from product import multiply
from division import divide

def main():
    print("Welcome to the Arithmetic Calculator!")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("5 / 3 =", divide(5, 3))
    print("5 / 0 =", divide(5, 0))  # Shows error handling for division by zero

if __name__ == "__main__":
    main()
