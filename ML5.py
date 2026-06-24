import pandas as pd
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("--- First Five Records ---")
print(df.head())
print("\n--- Dataset Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\n--- Column Names ---")
print(list(df.columns))
print("\n--- Missing Values Count ---")
print(df.isnull().sum())
print("\n--- Summary Statistics ---")
print(df.describe())
print("\n--- Class Distribution ---")
species_mapping = {i: name for i, name in enumerate(iris.target_names)}
class_counts = df['target'].map(species_mapping).value_counts()
print(class_counts)
