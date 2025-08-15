# covid_analysis.py

# ---------------------------
# 1. Import Libraries
# ---------------------------
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure plots display without errors
plt.rcParams['axes.unicode_minus'] = False

# ---------------------------
# 2. Load Dataset
# ---------------------------
data_path = r"C:\Users\kulal\data%20Analysis\cleaned_dataset.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError(f"CSV file not found at: {data_path}")

df = pd.read_csv(data_path)

# ---------------------------
# 3. Data Cleaning
# ---------------------------
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.fillna(0, inplace=True)

# ---------------------------
# 4. Quick Data Summary
# ---------------------------
print("\n--- Data Overview ---")
print(df.head())
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("\n--- Basic Stats ---")
print(df.describe())

# ---------------------------
# 5. Global Confirmed Cases Trend
# ---------------------------
plt.figure(figsize=(10,5))
df.groupby('Date')['Confirmed'].sum().plot()
plt.title("Global COVID-19 Confirmed Cases Over Time", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.grid(True)
plt.tight_layout()
plt.savefig("global_cases_trend.png")
plt.show()

# ---------------------------
# 6. Top 10 Countries by Total Confirmed Cases
# ---------------------------
top_countries = df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
top_countries.plot(kind='bar', color='orange')
plt.title("Top 10 Countries by Total Confirmed Cases", fontsize=14)
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("top10_countries.png")
plt.show()

# ---------------------------
# 7. Save Clean Data
# ---------------------------
cleaned_path = "cleaned_covid19_data.csv"
df.to_csv(cleaned_path, index=False)
print(f"\nCleaned dataset saved as: {cleaned_path}")

# ---------------------------
# 8. End Message
# ---------------------------
print("\n✅ Analysis complete. Graphs saved as PNG. Data cleaned and ready for Azure upload.")
