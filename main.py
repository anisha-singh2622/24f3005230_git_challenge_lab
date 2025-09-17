from sum import add
from difference import subtract
from product import multiply

def main():
    print("Welcome to the Arithmetic Calculator!")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))

if __name__ == "__main__":
    main()
