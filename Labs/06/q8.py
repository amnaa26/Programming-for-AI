import pandas as pd

#a. Load both CSV files into separate Pandas DataFrames.
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

#b. Display the first 5 and last 10 rows of each DataFrame to get an overview of the data.
print("Products DataFrame:")
print(products.head())
print(products.tail(10))
print("\nOrders DataFrame:")
print(orders.head())
print(orders.tail(10))

#c. Calculate and display the total revenue generated from all orders.
orders = orders.merge(products[['ProductID', 'Price']], on='ProductID')
orders['TotalRevenue'] = orders['Quantity'] * orders['Price']
total_revenue = orders['TotalRevenue'].sum()
print(f"\nTotal Revenue: ${total_revenue:.2f}")

#d. Find the top 5 best-selling products and top 5 low selling products.
best_selling = orders.groupby('ProductID')['Quantity'].sum().nlargest(5)
low_selling = orders.groupby('ProductID')['Quantity'].sum().nsmallest(5)
print("\nTop 5 Best-Selling Products:")
print(best_selling)
print("\nTop 5 Low Selling Products:")
print(low_selling)

#e. Determine the most common product category among the top 5 best-selling products.
top_selling_ids = best_selling.index
top_selling_categories = products[products['ProductID'].isin(top_selling_ids)]['Category']
most_common_category = top_selling_categories.mode()[0]
print(f"\nMost Common Product Category among Top 5 Best-Selling Products: {most_common_category}")

#f. Calculate and display the average price of products in each category.
average_price = products.groupby('Category')['Price'].mean()
print("\nAverage Price of Products in Each Category:")
print(average_price)

#g. Find the day, month and year separately with the highest total revenue.
orders['OrderDate'] = pd.to_datetime(orders['OrderDate'], format='%m-%d-%Y')
revenue_by_day = orders.groupby(orders['OrderDate'].dt.date)['TotalRevenue'].sum()
revenue_by_month = orders.groupby(orders['OrderDate'].dt.to_period('M'))['TotalRevenue'].sum()
revenue_by_year = orders.groupby(orders['OrderDate'].dt.year)['TotalRevenue'].sum()

highest_day = revenue_by_day.idxmax()
highest_month = revenue_by_month.idxmax()
highest_year = revenue_by_year.idxmax()

print(f"\nDay with Highest Total Revenue: {highest_day}")
print(f"Month with Highest Total Revenue: {highest_month}")
print(f"Year with Highest Total Revenue: {highest_year}")

#h. Create a new DataFrame that shows the total revenue for each month.
monthly_revenue = revenue_by_month.reset_index()
monthly_revenue.columns = ['Month', 'TotalRevenue']
print("\nTotal Revenue for Each Month:")
print(monthly_revenue)

#i. Check if the data has any null values or invalid characters, if present then clean that data accordingly.
products.dropna(inplace=True)
orders.dropna(inplace=True)

invalid_prices = products[~products['Price'].astype(str).str.match(r'^\d+(\.\d{1,2})?$')]
if not invalid_prices.empty:
    print("\nInvalid Prices Found:")
    print(invalid_prices)
    products.loc[invalid_prices.index, 'Price'] = None
    products.dropna(subset=['Price'], inplace=True)

print("\nFinal Products DataFrame after cleaning:")
print(products.info())
print("\nFinal Orders DataFrame after cleaning:")
print(orders.info())