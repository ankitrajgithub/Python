# if __name__ == __main__ : (This script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing.

def favourite_food(food):
    print(f'Your favourite food is {food}')

def main():
    print("This is main function")
    favourite_food("Pizza")
    print("Good bye")

print(__name__)

if __name__=='__main__':
    main()