import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read Excel files
df_small = pd.read_excel('Smallcap_Vol_shockers_above_30WMA.xls')
df_mid = pd.read_excel('Midcap_Vol_shockers_above_30WMA.xls')

# Aggregate counts by date
agg_small = df_small.groupby('date')['date'].count()
agg_mid = df_mid.groupby('date')['date'].count()

# Plot both datasets
plt.figure(figsize=(10, 6))
agg_small.plot(kind='bar', color='blue', alpha=0.6, label='Smallcap')
agg_mid.plot(kind='bar', color='orange', alpha=0.6, label='Midcap')

# Labels and title
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Smallcap vs Midcap Accumulation Data')
plt.legend()

# Adjust subplot parameters
plt.subplots_adjust(left=0.08, right=0.9, top=0.75, bottom=0.3)

# Generate timestamped filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f'Smallcap_vs_Midcap_Accumulation.png'

# Save plot
plt.savefig(filename)
print(f"Chart saved as {filename}")

