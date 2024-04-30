# This module contains functions for getting sales data from a user

def get_amount() -> float:
    """
    Gets a sales amount from the user, converts it to a
    float value, and returns the float value.
    """
    amount = float(input("Amount:           "))
    return amount

def get_month() -> int:
    """
    Gets a month from the user, converts it to an
    int value, and returns the int value
    """
    month = float(input("Month:           "))
    return month

def get_day() -> int:
    """
    Gets a day from the user, converts it to an
    int value, and returns the int value
    """
    day = float(input("Day:           "))
    return day

def get_year() -> int:
    """
    Gets a year from the user, converts it to an
    int value, and returns the int value
    """
    year = float(input("Year:           "))
    return year
