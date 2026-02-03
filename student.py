import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print("Average:", np.mean(data["Marks"]))
print("Highest:", np.max(data["Marks"]))
print("Lowest:", np.min(data["Marks"]))

pass_percentage = (data["Marks"] >= 35).mean() * 100
print("Pass Percentage:", pass_percentage)

plt.bar(data["Name"], data["Marks"])
plt.title("Student Performance Analysis")
plt.show()
