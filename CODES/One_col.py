import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("d.csv")
col = "Q13.10Duration spent ON watching TV"
write = "time spent in watching TV eah day"
# Extract the column to analyze
column_to_analyze = df[col].tolist()


# Initialize dictionary to count phone type categories
phone_type_count = {
    "Below 2 hours":0,
    "Upto 4 hours":0,
    "Upto 4 to 6 hours":0,
    "More than 6 hours":0,
    "Any other":0
}
total_count = len(column_to_analyze)
for c in column_to_analyze:
    if c==1:
        phone_type_count["Below 2 hours"] += 1
    elif c== 2:
        phone_type_count["Upto 4 hours"] += 1
    elif c== 3:
        phone_type_count["Upto 4 to 6 hours"] += 1
    elif c==4:
        phone_type_count["More than 6 hours"] += 1
    else:
        phone_type_count["Any other"] += 1

phone_type_percentages = {key: (value / total_count) * 100 for key, value in phone_type_count.items()}

# Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(phone_type_count.keys(), phone_type_count.values(), color=['#800020', '#4682B4', '#D3D3D3', '#008080'])
plt.xlabel('Time duration')
plt.ylabel('Count')
plt.title(f"Distribution of {write} by the population at the time of pandemic.\n\n")

for bar, phone_type in zip(bars, phone_type_count.keys()):
    height = phone_type_count[phone_type]
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}\n({phone_type_percentages[phone_type]:.0f}%)',ha='center', va='bottom')

# Set custom x-axis labels
plt.xticks(rotation=15)  # Rotate the labels for better visibility
plt.tight_layout()
plt.show()

# Print counts and percentages
for phone_type, count in phone_type_count.items():
    print(f"{phone_type}: {count} ({phone_type_percentages[phone_type]:.0f}%)")
