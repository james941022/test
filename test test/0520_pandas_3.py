import pandas as pd
file_name = 'SuperMarket Analysis.csv'
df = pd.read_csv(file_name)
print("1. 資料初步檢視 ")
print(f"資料總筆數: {len(df)} 筆")
print("\n前 3 筆資料內容 ")
print(df.head(3))
if 'Alex' in df['Branch'].values:
    df['Branch_Standard'] = df['Branch'].map({'Alex': 'A', 'Cairo': 'B', 'Giza': 'C'})
else:
    df['Branch_Standard'] = df['Branch']
filtered_df = df[(df['Branch_Standard'] == 'A') & (df['Customer type'] == 'Member')]

print("\n2. 資料篩選結果 ")
print(f"Branch 為 A 且 Customer type 為 Member 的交易筆數: {len(filtered_df)} 筆")
prod_summary = df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2)

print("\n 3. 各產品線銷售與評分彙總")
print(prod_summary)
city_gender_summary = df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Sales', 'count')
).round(2)

print("\n 4. 依 City 與 Gender 分組之分析結果 ")
print(city_gender_summary)
highest_sales_product = prod_summary['Total_Sales'].idxmax()
highest_sales_value = prod_summary['Total_Sales'].max()

print("\n 5. 銷售冠軍產品線 ")
print(f"總銷售額最高的產品線為: {highest_sales_product}")
print(f"該產品線總銷售額為: ${highest_sales_value}")
output_file = '0520_pandas_3OK.CSV'
prod_summary.to_csv(output_file, float_format='%.2f')
print(f"\n[狀態提示] 成功將產品線彙總結果匯出至 '{output_file}'。")