import pandas as pd

df = pd.read_csv("auto.csv")

# 1. Clean and update CSV
df.dropna(inplace=True)

# 2. Find most expensive car company
most_expensive = df.loc[df['price'].idxmax()]['company']
print("Most expensive car company:", most_expensive)

# 3. Print all Toyota car details
print(df[df['company'] == 'Toyota'])

# 4. Total cars count
print("Total cars:", df.shape[0])

# 5. Highest priced car
print(df.loc[df['price'].idxmax()])

# 6. Average mileage of all companies
print("Average mileage:", df['average-mileage'].mean())

# 7. Sort by price
df_sorted = df.sort_values(by='price')
print(df_sorted)
