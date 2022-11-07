#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Oct 2022
# This program finds the average of 3 numbers between 0-100


def main():

    # input
    string_1 = input("Enter in your first integer between 0-100: ")
    string_2 = input("Enter in your second integer between 0-100: ")
    string_3 = input("Enter in your third integer between 0-100: ")
    print("")

    # process
    try:
        integer_1 = int(string_1)
        integer_2 = int(string_2)
        integer_3 = int(string_3)
        if integer_1 and integer_2 and integer_3 >= 0:
            if integer_1 and integer_2 and integer_3 <= 100:
                add_int = integer_1 + integer_2 + integer_3
                add_int = add_int / 3
                print(
                    "The average of {0}, {1}, and {2}, is {3:,.3F}".format(
                        integer_1, integer_2, integer_3, add_int
                    )
                )
            else:
                print("One or more of your numbers are higher than 100, try again.")
        else:
            print("One or more of your numbers are less than 0, try again.")
    except ValueError:
        print("Invalid input, please input a integer between 0-100.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
