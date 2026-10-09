import pandas as pd

df = pd.read_csv('pixel_cafe_sales.csv')#dataframe 
print(df)#will print table of data to terminal 
print(df.shape)
print(df.columns)
print(df[["Product", "Quantity"]])
food = df[df["Category"] == "Food"]
print(food)
busy = df[df["Quantity"] > 30]
print(busy)
both = df[(df["Quantity"] > 30) & (df["Category"] == "Food")]
print(both)
