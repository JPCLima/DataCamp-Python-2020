# Printing dates in a friendly format
# Assign the earliest date to first_date
from datetime import date
first_date = sorted(florida_hurricane_dates)[0]

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime('%m/%d/%Y')

print("ISO: " + iso)
print("US: " + us)

# Representing dates in different ways
# Import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))

# Import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))

# Import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))
