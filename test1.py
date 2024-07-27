import pandas as pd
import matplotlib.pyplot as plt
data = {'Name': ['John', 'Vihan', 'Krishna', 'Arithi'],
    'Social': [50,95,56,60],
    'English': [50,85,89,87],
    'Hindi': [59,73,64,91],
    'Maths': [75,75,96,87],
    'Science': [95,50,65,90]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
pivot_table = df.melt(['Name'], var_name='Subject', value_name='Score')
pivot_table = pivot_table.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')
print("\nPivot Table:")
print(pivot_table)
df['Total'] = df[['Social', 'English', 'Hindi', 'Maths', 'Science']].sum(axis=1)
print("\nDataFrame with Total Scores:")
print(df)
sorted_df = df[df['English'] > 80].sort_values(by='English', ascending=False)
print("\nSorted DataFrame (English > 80):")
print(sorted_df)
df.plot(kind='bar', x='Name', y=['Social', 'English', 'Hindi', 'Maths', 'Science'], stacked=True)
plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Student Scores by Subject')
plt.show()



