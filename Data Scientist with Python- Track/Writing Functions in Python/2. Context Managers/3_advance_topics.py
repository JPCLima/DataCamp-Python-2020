# Scraping the NASDAQ
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
    # Open "NVDA.txt" for writing as f_out
    with open('NVDA.txt', 'w') as f_out:
        for _ in range(10):
            value = nvda.price()
            print('Logging ${:.2f} for NVDA'.format(value))
            f_out.write('{:.2f}\n'.format(value))


# Changing the working directory
def in_dir(directory):
    """Change current working directory to `directory`,
    allow the user to run some code, and change back.

    Args:
      directory (str): The path to a directory to work in.
    """
    current_dir = os.getcwd()
    os.chdir(directory)

    # Add code that lets you handle errors
    try:
        yield
    # Ensure the directory is reset,
    # whether there was an error or not
    finally:
        os.chdir(current_dir)
