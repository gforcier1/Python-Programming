#! /usr/bin/env python3

print()
print("SALES DATA IMPORTER")

print()
print("Enter sales data")

#Variable to accumulate the total sales amount
total = 0.0

# Get the sales for the first day
amount_1 = float(input("Amount:      "))
year_1 = int(input("Year:      "))
month_1 = int(input("Month:      "))
day_1 = int(input("Day:      "))
print()

# Add sales to total
total += amount_1

# display sales info
print(f"1.\t\t{year_1}-{month_1}-{day_1}\t${amount_1}\n")

# Get the sales for the second day
amount_2 = float(input("Amount:      "))
year_2 = int(input("Year:      "))
month_2 = int(input("Month:      "))
day_2 = int(input("Day:      "))
print()

# Add sales to total
total += amount_2

# display sales info
print(f"2.\t\t{year_2}-{month_2}-{day_2}\t${amount_2}\n")

# Get the sales for the third day
amount_3 = float(input("Amount:      "))
year_3 = int(input("Year:      "))
month_3 = int(input("Month:      "))
day_3 = int(input("Day:      "))
print()

# Add sales to total
total += amount_3

# display sales info
print(f"3.\t\t{year_3}-{month_3}-{day_3}\t${amount_3}\n")

# Display the total
print("Total Sales")
print()
print(f"${total}\n")

print("Bye")
