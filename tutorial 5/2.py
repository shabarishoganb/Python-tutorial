import pandas as pd

data = [[1, 'Alice', 24], [2, 'Bob', 27], [3, 'Charlie', 22]]
df = pd.DataFrame(data, columns=['ID', 'Name', 'Age'])
df.set_index('ID', inplace=True)
print(df)
