import pandas as pd

# Load employee.csv file (assuming it exists)
df = pd.read_csv("employee.csv")

# 1. Print first 7 records
print(df.head(7))

# 2. Print all employee names in alphabetical order
print(df['name'].sort_values())

# 3. Find the employee with the highest salary
highest_salary_emp = df.loc[df['salary'].idxmax(), 'name']
print("Employee with highest salary:", highest_salary_emp)

# 4. List names of male employees
male_employees = df[df['gender'] == 'Male']['name']
print("Male Employees:\n", male_employees)

# 5. Display all teams employees belong to
print("Teams:\n", df['team'].unique())
