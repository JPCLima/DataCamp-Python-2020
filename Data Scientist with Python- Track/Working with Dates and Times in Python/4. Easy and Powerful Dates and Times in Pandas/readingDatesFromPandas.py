# Loading a csv file in Pandas
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])

# Making timedelta columns
# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())
