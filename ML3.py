import pandas as pd
data = {
    'Roll No': [101, 102, 103, 104, 105],
    'Name': ['Ravi', 'Priya', 'Kiran', 'Anu', 'Sita'],
    'Marks': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)
print(df)
print("\n")
print("First three records")
print(df.head(3))
print("\n")

avg_marks = df['Marks'].mean()
print(f"--- 3. Average Marks ---\n{avg_marks}\n\n")

highest_marks_student = df.loc[df['Marks'].idxmax()]
print(highest_marks_student)
print("\n")

lowest_marks_student = df.loc[df['Marks'].idxmin()]
print(lowest_marks_student)
print("\n")

def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Marks'].apply(assign_grade)

print("6. DataFrame with Grades")
print(df)
