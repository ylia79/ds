import pandas as pd
import matplotlib.pyplot as plt
import sweetviz as sv
import geopandas as gpd
import pycountry

# Set the file path
file_path = "small_dataset.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Analyze the dataframe and generate a report
report = sv.analyze(df)

# Display the report in an HTML file
report.show_html("sweetviz_report.html")

# Create a histogram of ages
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Import world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Count the number of occurrences for each country
country_counts = df['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

# Merge the country counts with the world map data
world = world.merge(country_counts, how='left', left_on='name', right_on='Country')

# Plot the distribution of people by country
fig, ax = plt.subplots(1, 1, figsize=(15, 18))
world.plot(column='Count', ax=ax, legend=True, legend_kwds={ 'label': "Number of People by Country"})
plt.title('Distribution of People by Country')
plt.show()

def get_country_code(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except AttributeError:
        return None

# Add country codes to the dataframe
df['Country Code'] = df['Country'].apply(get_country_code)

# Print the modified dataframe with country codes
print("Modified DataFrame with Country Codes:")
print(df[['ID', 'Country', 'Country_Code']])

# Save the modified dataframe to a CSV file
df.to_csv("modified_dataset.csv", index=False)
