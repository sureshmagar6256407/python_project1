import calendar

try:
    year = int(input("Enter year (e.g., 2024): "))
    month = int(input("Enter month (1-12): "))

    if 1 <= month <= 12:
        print("\n", calendar.month(year, month))
    else:
        print("Please enter a valid month between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter numbers only.")
