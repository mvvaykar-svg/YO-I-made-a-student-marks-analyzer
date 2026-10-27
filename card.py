import pandas as pd

# Student Data
data = {
    "Name": ["Viraj", "Rahul", "Aman", "Priya", "Neha"],
    "Math": [95, 78, 88, 45, 67],
    "Science": [92, 85, 90, 40, 72],
    "English": [89, 80, 85, 55, 76]
}

df = pd.DataFrame(data)

# Calculation
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3
df["Average"] = df["Average"].round(2)

# Pass / Fail Logic
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 35 else "Fail")

# Grade Logic - Simple
df["Grade"] = df["Average"].apply(
    lambda x: "A" if x >= 85 else "B" if x >= 60 else "C" if x >= 35 else "Fail"
)

# Topper
topper = df.loc[df["Total"].idxmax()]

# Output
print("===== STUDENT MARKS ANALYZER =====")
print(df.to_string(index=False))

print("\n--- Class Report ---")
print(f"Class Average: {df['Average'].mean():.2f}")
print(f"Topper: {topper['Name']} - {topper['Total']} Marks")
print(f"Highest Score: {topper['Total']}")

print("\n--- Result Count ---")
print(df["Result"].value_counts())

print("\n--- Grade Count ---")
print(df["Grade"].value_counts())