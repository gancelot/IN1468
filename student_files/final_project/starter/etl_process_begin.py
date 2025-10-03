import matplotlib.pyplot as plt
import pandas as pd

import acquire_customer_info
import read_sales

# Step 12. Call get_sales() from the read_sales module (already imported).  Also,
# call get_customers() from the acquire_customer_info module (already imported).
# Finally, call customers_to_dataframe() from the acquire_customer_info module and
# pass the list of customers into it.



# Step 13. We don't have a lot of data cleaning to perform here.  So, we'll simply
# convert the 'sale_date' column to a DateTime object using pd.to_datetime():
#        sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'])

# Step 14. Merge the sales_data and customers dataframes using pd.merge() as shown:
#        merged_data = pd.merge(sales_data, customers_df, on='customer_id', how='left')
# Note: make adjustments to variable names if you used different names.


# Step 15. Group together records after merging them by customer_id.
# Then use the agg() method to aggregate several summary operations:
# 1) sum of total_amount values per customer
# 2) sum of total_quantity values per customer
# Hint:
#  merged_data.groupby(['customer_id']).agg(total_sales=('total_amount', 'sum'), total_quantity=('quantity', 'sum'))


# Step 16. Save the results to a Datafile (your choice of name) and plot it
# using Matplotlib.  THe Matplotlib statements are provided below:
#     plt.bar(report_data.index, report_data.get('Total Sales Amount'))
#     plt.show()

# Also, print the results to the console.