
# ✅ Task 1: Load and Explore the Dataset

# For this project, I used the Iris dataset from scikit-learn, which includes measurements of iris flowers from three species.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map(dict(enumerate(iris.target_names)))
except Exception as e:
    print("There was an error loading the dataset:", e)
    exit()

# Preview the first few rows to understand the structure
print("Preview of the dataset:")
print(df.head())

# Check the data types and look for any issues
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values check:")
print(df.isnull().sum())

# Clean the data (not needed here but included for practice)
df_cleaned = df.dropna()

# ✅ Task 2: Basic Data Analysis

# Summary statistics
print("\nDescriptive statistics:")
print(df_cleaned.describe())

# Group by species and compute mean of each feature
grouped = df_cleaned.groupby("species").mean()
print("\nMean values grouped by species:")
print(grouped)

# Insight based on analysis
print("\nObservation:")
print("Setosa has the smallest petal measurements among all species, making it easily distinguishable.")

# ✅ Task 3: Data Visualization

sns.set(style="whitegrid")

# 1. Line Chart - Sepal Length Across Samples
plt.figure(figsize=(10, 5))
plt.plot(df_cleaned.index, df_cleaned['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average Petal Length by Species
plt.figure(figsize=(8, 5))
sns.barplot(data=df_cleaned, x='species', y='petal length (cm)', palette='muted')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram - Sepal Width Distribution
plt.figure(figsize=(8, 5))
plt.hist(df_cleaned['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_cleaned, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
