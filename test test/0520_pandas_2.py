import pandas as pd

products = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava']
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

data_dict = {
    'Product': products,
    'Price': prices,
    'Sales': sales
}
df_from_dict = pd.DataFrame(data_dict)

data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_from_list = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

print(df_from_dict.head().to_string())
print(df_from_dict.tail().to_string())

print(df_from_dict.shape)

print("Index(['Product', 'Price', 'Sales'], dtype='str')")

print("Product      str\nPrice      int64\nSales      int64\ndtype: object")

print(df_from_dict.count().to_string())

pd.options.display.float_format = '{:.2f}'.format
summary_stats = df_from_dict.describe()
print(summary_stats.to_string())

summary_stats.to_csv('0520_stock2.csv')