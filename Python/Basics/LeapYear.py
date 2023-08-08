def is_leap(year):
    leap = False  # Initialize leap to False, assuming it's not a leap year by default

    # Check if the year is divisible by 4
    if (year % 4) == 0:
        leap = True  # If it's divisible by 4, set leap to True (potential leap year)

        # Check if the year is also divisible by 100
        if (year % 100) == 0:
            leap = False  # If it's divisible by 100, set leap back to False (potential non-leap year)

            # Check if the year is divisible by 400
            if (year % 400) == 0:
                leap = True  # If it's divisible by 400, set leap back to True (leap year)

    return leap  # Return the final value of leap, True for leap year, False for non-leap year

# Get the input year from the user
year = int(input())

# Call the is_leap function with the provided year and print the result
print(is_leap(year))
