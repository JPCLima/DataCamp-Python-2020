# Extract a function
def standardize(column):
    """Standardize the values in a column.

    Args:
      column (pandas Series): The data to standardize.

    Returns:
      pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)

# Split up a function


def median(values):
    """Get the median of a list of values

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float
    """
    # Write the median() function
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]
    return median
