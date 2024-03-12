import pyforest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import dtale
import plotly.express as px

# Set the file path
file_path = "different_dataset.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the dataframe summary
df.describe()

# Visualize the dataframe using dtale
dtale.show(df)

# Prepare the data for modeling
X = df[['Experience']]
y = df['Salary']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=None)  # Set test_size to None

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate Mean Squared Error and R-squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')

# Visualize the linear regression line using Plotly
fig = px.scatter(x=X_test['Experience'], y=y_test, title='Linear Regression: Experience vs Salary', labels={'x': 'Experience', 'y': 'Salary'})
fig.add_scatter(x=X_test['Experience'], y=y_pred, mode='lines', name='Regression Line', line=dict(color='red'))
fig.show()
