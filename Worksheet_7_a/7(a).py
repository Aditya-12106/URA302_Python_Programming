import pandas as pd

#Part 1.1
print(pd.__version__)

#Part 1.2
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

#Part 2.1
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)

#Part 2.2
second_element = S1[1]
fourth_element = S1[3]

print(f"Second element: {second_element}")
print(f"Fourth element: {fourth_element}")

#Part 2.3
S2 = pd.Series([10, 20, 30, 40, 50])
result = S1 + S2
print(result)

#Part 3.1
print(df[['Name', 'City']])

#Part 3.2
df['Salary'] = [50000, 60000, 70000]
print(df)

#Part 3.3
average_age = df['Age'].mean()
print(f"Average Age: {average_age}")

total_salary = df['Salary'].sum()
print(f"Total Salary: {total_salary}")

#Part 4.1
filtered_df = df[df['Age'] > 28]
print(filtered_df)

#Part 4.2
df_with_index = df.set_index('Name')

print("DataFrame with 'Name' as index:")
print(df_with_index)

df_reset_index = df_with_index.reset_index()
print("\nDataFrame after resetting the index:")
print(df_reset_index)

#Part 5.1
df_employees = pd.read_csv('employees.csv')
print(df_employees)

#Part 5.2
filtered_employees = df_employees[df_employees['Salary'] > 55000]
print(filtered_employees[['Name', 'Department']])

#Part 6.1
avg_salary_by_dept = df_employees.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)

#Part 6.2
salary_min_max_by_dept = df_employees.groupby('Department')['Salary'].agg(['min', 'max'])
print(salary_min_max_by_dept)

#Part 7.1
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})

df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})

merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)

#Part 8.1
sorted_df = merged_df.sort_values(by='Experience (Years)', ascending=False)
print(sorted_df)