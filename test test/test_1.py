import pandas as pd

df = pd.DataFrame({

    "name": ["Amy", "Bob", "Cathy", "David", "Evan", "Fiona"],

    "age": [20, 21, 19, 22, 20, 23],

    "score": [88, 92, 79, 85, 90, 95]

})

print(df.describe().round(2))
#查看後5筆

