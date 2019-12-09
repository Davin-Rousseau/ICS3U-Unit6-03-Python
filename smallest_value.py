#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: December 2019
# This program uses an array
# to print out smallest value in a random list

import random


def minimum_number(list_of_numbers):
    # this function print smallest value in the list(array)

    min_number = list_of_numbers[0]

    for counter in list_of_numbers:
        if counter < min_number:
            min_number = counter

    return min_number


def main():
    # this function uses a list(array)

    random_numbers = []
    min_value = 0

    print("The numbers are: ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    min_value = minimum_number(random_numbers)

    print("")
    print("The smallest value in the list is: {0} ".format(min_value))


if __name__ == "__main__":
    main()
