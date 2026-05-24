import numpy as np
import csv
products = []
stock = []
prices = []
sales_volume = []
with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row["Product_Name"])
        stock.append(float(row["Stock_Quantity"]))
        prices.append(float(row["Unit_Price"].replace('$', '').strip()))
        sales_volume.append(float(row["Sales_Volume"]))
np_products = np.array(products)
np_stock = np.array(stock)
np_prices = np.array(prices)
np_sales_volume = np.array(sales_volume)
np_total_inventory_value = np_stock * np_prices

with open("All_Products_Inventory_Value.csv", "w", encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Product_Name", "Total_Inventory_Value"])
    for i in range(len(np_products)):
        writer.writerow([np_products[i], round(np_total_inventory_value[i], 2)])

print(" 已將每個商品的總庫存價值完整匯出至 'All_Products_Inventory_Value.csv'")
best_selling_idx = np.argmax(np_sales_volume)
best_selling_product = np_products[best_selling_idx]
best_selling_volume = np_sales_volume[best_selling_idx]

print(f" 最暢銷商品: {best_selling_product} (銷售量: {int(best_selling_volume)})")
np_discounted_revenue = np_sales_volume * np_prices * 0.9
total_discounted_revenue = np.sum(np_discounted_revenue)
print(f" 所有商品9折後的總收入為: ${total_discounted_revenue:,.2f}")