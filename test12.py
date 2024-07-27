import pandas as pd
import matplotlib.pyplot as plt
data = {'Employer':[ 'Roshon', 'Amar', 'Lohith', 'Ashwini', 'Mohan', 'Pramod'],
    'Department': ['CS', 'CS', 'EC', 'EC', 'CS', 'EC'],
    'Experience': [10, 15, 5, 14, 20, 14],
    'Type': ['Regular', 'Adhoc', 'Regular', 'Contract', 'Regular', 'Contract'],
    'Salary': [50000, 20000, 15000, 30000, 40000, 15000]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
pivot_avg_salary = df.pivot_table(index='Department', columns='Employer', values='Salary', aggfunc='mean')
print("\nPivot Table (Average Salary by Department):")
print(pivot_avg_salary)
pivot_salary_summary = df.pivot_table(index='Type', columns='Department', values='Salary', aggfunc=['sum', 'mean'])
print("\nPivot Table (Salary Summary by Type and Department):")
print(pivot_salary_summary)
pivot_avg_salary.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.title('Average Salary by Department')
plt.legend(title='Employer')
plt.show()
pivot_salary_summary['sum'].plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Type')
plt.ylabel('Total Salary')
plt.title('Total Salary by Department')
plt.legend(title='Department')
plt.show()
pivot_salary_summary['mean'].plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Type')
plt.ylabel('Average Salary')
plt.title('Average Salary by  Department')
plt.legend(title='Department')
plt.show()

