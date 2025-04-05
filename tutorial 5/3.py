import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [24, 27]}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)
print("Data written to output.xlsx")
