# Which avocado size is most popular?
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()


# Changes in sales over time
# Import matplotlib.pyplot with alias plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()

# Avocado supply and demand
# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x="nb_sold", y="avg_price",
              title="Number of avocados sold vs. average price", kind="scatter")

# Show the plot
plt.show()


# Price of conventional vs. organic avocados
# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(
    bins=20, alpha=0.5)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins=20, alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
