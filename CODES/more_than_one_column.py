import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("d.csv")
columns_to_analyze = ["14.2/1 Ivermectin", "14.2/2 Azithromycin", "14.2/3 Favipiravir", "14.2/4 Albendazole","14.2/5 Remdesivir","14.2/6 Hydroxychloroquine","14.2/7 Any other"]

# Calculate the sum for each source
count_of_data = {source: df[source].sum() for source in columns_to_analyze}
total_count = 999
percentage = {k.split('/')[1][1:]: float(v / total_count * 100) for k, v in count_of_data.items()}

# Plot the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(percentage.keys(), percentage.values(), color=['#800020', '#4682B4', '#D3D3D3', '#008080', '#808000', '#483C32'])

# Add annotations for each bar
for i, bar in enumerate(bars):
    yval = bar.get_height()
    source_name = columns_to_analyze[i]
    label = f"{yval:.2f}% ({count_of_data[source_name]})"
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, label, ha='center', va='bottom')

plt.xlabel("\nKinds of medicines")
plt.ylabel("Percentage of population")
plt.title("Distribution of kinds of medicines intake by the population.\n\n")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print the collective percentage of social media used by the population
print("Collective percentage of social media used by the population:")
for source, percent in percentage.items():
    print(f"{source}: {percent:.2f}%, total count is: {count_of_data['14.2/' + str(list(percentage.keys()).index(source) + 1) + source]}")



