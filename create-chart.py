import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('Smallcap_Vol_shockers_above_30WMA.xls')

md = pd.read_excel('Midcap_Vol_shockers_above_30WMA.xls')
# Aggregate column data
agg_data = df.groupby('date')['date'].count()  # Replace 'group_column' and 'value_column' with your column names

# Aggregate column data
agg_data = md.groupby('date')['date'].count()  # Replace 'group_column' and 'value_column' with your column names

# Create bar chart
agg_data.plot(kind='bar')


# Add labels and title
plt.xlabel('Date')
plt.ylabel('Number of Count')
plt.title('Smallcap Accumulation Data')

# Adjust subplot parameters
plt.subplots_adjust(left=0.08, right=0.9, top=0.75, bottom=0.3)  # Adjust as needed


# Generate timestamp
timestamp1 = datetime.now().strftime("%Y%m%d_%H%M%S")
timestamp = datetime.now().strftime("%Y%m%d")
print("Current Time =", timestamp)
# Save the plot to a file with timestamp appended
filename = 'Smallcap_Accumulation_data_'+ (str(timestamp1)) +'.png'
plt.savefig(filename)  # Save as PNG file


# Show the plot
plt.show()
