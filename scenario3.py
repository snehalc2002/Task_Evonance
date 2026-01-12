"""
Task: A dataset has missing values in the "income" column. Write code to:

1. Replace missing values with the median if the data is normally distributed.

2. Replace with the mode if skewed.
Use Pandas and a skewness threshold of 0.5."""

import pandas as pd


df = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'income': [30000, None, 32000, 31000, None, 70000]
})


skew_val = df['income'].skew()

if abs(skew_val) < 0.5:
    fill_value = df['income'].median()
    print(f"Skew: {skew_val:.2f} → Filling missing values with median: {fill_value}")
else:
    fill_value = df['income'].mode()[0]
    print(f"Skew: {skew_val:.2f} → Filling missing values with mode: {fill_value}")


df['income'] = df['income'].fillna(fill_value)


print(df)
