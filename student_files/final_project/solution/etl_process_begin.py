import matplotlib.pyplot as plt
import pandas as pd

import acquire_customer_info
import read_sales

# Gather data
sales_data = read_sales.get_sales()
customers = acquire_customer_info.get_customers()
customers_df = acquire_customer_info.customers_to_dataframe(customers)

# Data Cleaning
sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'])

# Data Enrichment - Merging DataFrames
merged_data = pd.merge(sales_data, customers_df, on='customer_id', how='left')

# Calculating New Metrics
customer_sales_summary = merged_data.groupby(['customer_id']).agg(
    total_sales=('total_amount', 'sum'), total_quantity=('quantity', 'sum'))

report_data = customer_sales_summary.rename(
    columns={
        'total_sales': 'Total Sales Amount',
        'total_quantity': 'Total Quantity Sold'
    })

# Save Results to a Datafile and Plot It
report_data.to_csv('customer_sales_report.csv', index=False)
plt.bar(report_data.index, report_data.get('Total Sales Amount'))
plt.show()

print(report_data)