# Pivoting on one variable
import numpy as np
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)


# Fill in missing values and sum values with pivot tables
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='department',
                        index='type', columns='weekly_sales', fill_value=0))
