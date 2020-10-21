# Annotating a plot of time-series data
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change.relative_temp)

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(">1 degree", (pd.Timestamp('2015-10-06'), 1))

plt.show()

# Plotting time-series: putting it all together
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index,
                climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index,
                climate_change['relative_temp'], 'red', "Time (years)", "Relative temp (Celsius)")
