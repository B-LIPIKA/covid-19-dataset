import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv(r"C:\Users\kulal\data%20Analysis\cleaned_dataset.csv")

# 2. Data cleaning
df['Date'] = pd.to_datetime(df['Date'])
df.fillna(0, inplace=True)

# 3. Visualization: Global confirmed cases
plt.figure(figsize=(10,5))
df.groupby('Date')['Confirmed'].sum().plot()
plt.title("Global COVID-19 Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.grid(True)
plt.show()

# 4. Visualization: Top 10 countries
top_countries = df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(10)
top_countries.plot(kind='bar', figsize=(8,5), color='orange')
plt.title("Top 10 Countries by Total Confirmed Cases")
plt.ylabel("Confirmed Cases")
plt.show()
