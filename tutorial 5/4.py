import pandas as pd

data = {'City': ['New York', 'Los Angeles'], 'Population': [8419600, 3980400]}
df = pd.DataFrame(data)
df.to_excel("city_data.xlsx", index=False)
print("Data written to city_data.xlsx")
