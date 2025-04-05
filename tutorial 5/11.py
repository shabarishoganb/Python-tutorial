# Sample sales data
sales_data = {
    'month_number': [1, 2, 3, 4, 5, 6],
    'facecream': [2500, 2600, 2700, 2800, 2900, 3000],
    'facewash': [1500, 1600, 1700, 1800, 1900, 2000],
    'toothpaste': [5200, 5300, 5400, 5500, 5600, 5700],
    'bathingsoap': [9200, 9300, 9400, 9500, 9600, 9700],
    'shampoo': [1200, 1300, 1400, 1500, 1600, 1700],
    'moisturizer': [1500, 1600, 1700, 1800, 1900, 2000],
    'total_units': [25000, 26000, 27000, 28000, 29000, 30000],
    'total_profit': [20000, 22000, 24000, 26000, 28000, 30000]
}
df_sales = pd.DataFrame(sales_data)

# Scatter plot for toothpaste sales
plt.scatter(df_sales['month_number'], df_sales['toothpaste'], color='red')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Toothpaste Sales per Month')
plt.show()

# Bar chart for facecream and facewash
df_sales[['facecream', 'facewash']].plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream and Face Wash Sales')
plt.show()

# Pie chart for total product sales
total_sales = df_sales.iloc[:, 1:-2].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Product Sales Distribution')
plt.show()
