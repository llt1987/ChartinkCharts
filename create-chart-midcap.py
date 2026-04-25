import pandas as pd
import matplotlib.pyplot as plt

# Read your Excel file
df = pd.read_excel("Midcap_Vol_shockers_above_30WMA.xls")

# Ensure 'date' column is parsed as datetime
#df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y").dt.date


# Count occurrences of each sector per date
sector_counts = df.groupby(['date', 'sector']).size().unstack(fill_value=0)

# Plot stacked bar chart
sector_counts.plot(kind='bar', stacked=True, figsize=(12, 6))

# Labels and title
plt.xlabel("Date")
plt.ylabel("Count of Symbols")
plt.title("Accumulation Distribution by Date (Midcap)")
plt.legend(title="Sector", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout
plt.tight_layout()

# Save chart
plt.savefig("Midcap_Sector_Accumulation_Distribution.png")
print("Report saved as Midcap_Sector_Accumulation_Distribution.png")


