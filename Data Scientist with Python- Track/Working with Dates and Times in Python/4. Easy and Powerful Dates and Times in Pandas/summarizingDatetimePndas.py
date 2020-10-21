# How many joyrides?
# Create joyrides
import matplotlib.pyplot as plt
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"
      .format(rides[joyrides]['Duration'].median()))

# It's getting cold outside, W20529
# Import matplotlib

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date')\
    .size()\
    .plot(ylim=[0, 150])

# Show the results
plt.show()

# Members vs casual riders over time
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

# Combining groupby() and resample()
# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
    .resample('M', on='Start date')

# Print the median duration for each group
print(grouped['Duration'].median())
