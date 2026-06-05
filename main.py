import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/student_data.csv")

# Analysis
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("visualizations/bar_chart.png")
plt.close()

# Pie Chart
plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.savefig("visualizations/pie_chart.png")
plt.close()

print("Charts created successfully!")