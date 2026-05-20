import numpy as np
import csv

Reorder_Quantity = []
Sales_Volume = []
stock = []
discount = []

with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f) #DictReader = 用欄位名稱讀 CSV

    for row in reader:
        products.append(row["Product"])
        price.append(float(row["Price"]))
        stock.append([float(row["Stock_A"]),float(row["Stock_B"]),float(row["Stock_C"])])
        discount.append(float(row["Discount"]))