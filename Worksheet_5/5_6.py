import numpy as np

np.random.seed(42)
sales_data = np.random.randint(100, 500, (12, 4))

total_sales = np.sum(sales_data, axis=1)
average_sales = np.mean(sales_data, axis=0)

max_sales = np.max(sales_data)
min_sales = np.min(sales_data)

best_month = np.argmax(total_sales) + 1
worst_month = np.argmin(total_sales) + 1

print(f"Total sales per month: {total_sales}")
print(f"Average sales per product: {average_sales}")
print(f"Best month: Month {best_month}")
print(f"Worst month: Month {worst_month}")
