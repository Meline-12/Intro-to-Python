def calculate_cube(x):
    return x**3
def calculate_square(x):
    return x**2

from pretty_print import *

def main():
    simple_print(calculate_square(2))
    pro_print(calculate_cube(4))

if __name__ == "__main__":
    main()