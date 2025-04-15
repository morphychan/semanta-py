# main.py
# Entry point that uses mathlib functions and prints the results.

from mathlib import add, multiply

def main():
    """Execute basic math operations and display the results."""
    x = 3
    y = 5

    total = add(x, y)
    product = multiply(x, y)

    print("Sum:", total)
    print("Product:", product)

if __name__ == "__main__":
    main()