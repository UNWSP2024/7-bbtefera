# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def rainfall_statistics():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    rainfall = [float(input(f"Enter rainfall for {month}: ")) for month in months]

    total = sum(rainfall)
    avg = total / 12
    max_month, min_month = months[rainfall.index(max(rainfall))], months[rainfall.index(min(rainfall))]

    print(f"\nTotal: {total:.2f} inches, Avg: {avg:.2f} inches")
    print(f"Max: {max_month} ({max(rainfall):.2f} inches), Min: {min_month} ({min(rainfall):.2f} inches)")

rainfall_statistics()
