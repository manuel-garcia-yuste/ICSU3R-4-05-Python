#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program do a continue statement


def main():
    # function adds positive numbers

    # variables
    repeater = 0
    addNumber = 0
    answer = 0
    exception = False

    try:
        number = int(input("How many numbers to add: "))
        # process
        for repeater in range(number):
            # input
            addNumber = int(input("Enter a number: "))
            if addNumber < 0:
                continue
            else:
                answer = answer + addNumber
    except ValueError:
        exception = True
        print("Invalid input.")

    if exception is False:
        print("The answer is " + str(answer))


if __name__ == "__main__":
    main()
