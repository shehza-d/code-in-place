import random

def main():
    sides = int(input("How many sides does your dice have? "))
    print("Your roll is ", random.randint(1, sides))

if __name__ == '__main__':
    main()