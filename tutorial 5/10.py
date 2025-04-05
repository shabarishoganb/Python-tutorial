import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Create a sample stud.csv file
data = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'place': ['NY', 'LA', 'SF', 'TX', 'FL'],
    'mark': [85, 78, 92, 88, 76]
}
df = pd.DataFrame(data)
df.to_csv("stud.csv", index=False)

# Read and display file contents
df = pd.read_csv("stud.csv")
print(df)

# Set rollno as index
df.set_index('rollno', inplace=True)
print(df)

# Display name and mark
print(df[['name', 'mark']])

# Sort by name
print(df.sort_values(by='name'))

# Sort by mark in descending order
print(df.sort_values(by='mark', ascending=False))

# Compute statistics
print("Average:", df['mark'].mean())
print("Median:", df['mark'].median())
print("Mode:", stats.mode(df['mark'])[0][0])

print("Minimum Mark:", df['mark'].min())
print("Maximum Mark:", df['mark'].max())

print("Variance:", df['mark'].var())
print("Standard Deviation:", df['mark'].std())

# Display histogram of marks
plt.hist(df['mark'], bins=5, color='blue', edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Histogram of Marks')
plt.show()

# Remove 'place' column
df.drop(columns=['place'], inplace=True)
print(df)
