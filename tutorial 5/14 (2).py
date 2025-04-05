data = {
    'Reg_no': [10001, 10002, 10003],
    'Name': ['Jack', 'John', 'Alex'],
    'Sub_Mark1': [76, 77, 74],
    'Sub_Mark2': [88, 84, 79],
    'Sub_Mark3': [76, 79, 81]
}
df_marks = pd.DataFrame(data)
df_marks.to_csv("marks.csv", index=False)
