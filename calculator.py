#!/usr/bin/env python3
# Created by: Gustav I
# Created on: May 9, 2025
# This program is a calculator with different operations available


def calculate(sign, first_number, second_number):
    result = 0.0

    if sign == "+":
        result = first_number + second_number
    elif sign == "-":
        result = first_number - second_number
    elif sign == "*":
        result = first_number * second_number
    elif sign == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

    return result


def main():
    try:
        sign = input("Enter operation (+, -, *, /): ")

        if sign not in ["+", "-", "*", "/"]:
            raise ValueError("Invalid operation sign.")

        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        # Validate division by zero before calling the function
        if sign == "/" and second_number == 0:
            print("Error: Division by zero")
            return

        result = calculate(sign, first_number, second_number)
        print("Result:", result)

    except ValueError as e:
        print("Invalid input:", e)


# Run the program
main()
