# if __name__ == __main__ : (This script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing.
# Good Practice (Code is modular,
#                Helps readability,
#                Leaves no global variables,
#                Avoid unintended execution)

# Ex. library = Import library for functionality
#               When running the library directly, display a help page

def favourite_food(food):
    print(f'Your favourite food is {food}')

def main():
    print("This is main function")
    favourite_food("Pizza")
    print("Good bye")

print(__name__)

if __name__=='__main__':
    main()