#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 9, 2021
# This program takes a decimal number and rounds it to the number of decimals
# specified by the user

def round(number, decimals, user_num):
    # This function takes a number and the number of decimal places and then
    # rounds it to that number of places
    if (user_num < 0):
        # does this if the number is negative
        number[0] = number[0] * 10**decimals - 0.5
        number_cast = int(number[0])
        number[0] = number_cast / 10**decimals
    else:
        # does this if the number is positive
        number[0] = number[0] * 10**decimals + 0.5
        number_cast = int(number[0])
        number[0] = number_cast / 10**decimals


def main():
    # greet user
    print("This program rounds a decimal number to a number of places\
 entered.")

    while True:
        # get the decimal number
        user_num_string = input("Enter a decimal number: ")

        try:
            # convert from string to float
            user_num_float = float(user_num_string)
            break

        except ValueError:
            # error message of the input is not a number
            print("{} is not a number, try again.". format(user_num_string))
    print()

    while True:
        # gets the number of decimal places to round to
        user_dec_places_string = input("How many decimal places do you want\
 to round the number to? ")

        try:
            # convert from string to int
            user_dec_places_int = int(user_dec_places_string)
            if (user_dec_places_int < 0):
                # check if input is negative
                print("{} is a negative number, try again.\
". format(user_dec_places_int))
            else:
                break

        except ValueError:
            # error message if the input is not a valid integer
            print("{} is not a valid number, try again.\
". format(user_dec_places_string))
    print()

    # put the number into an array to pass by reference
    number_array = []
    number_array.append(user_num_float)

    # call round() to round the number
    round(number_array, user_dec_places_int, user_num_float)

    # display rounded number
    print("The number rounded is: {}". format(number_array[0]))
    print()


if __name__ == "__main__":
    main()
