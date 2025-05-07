import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv('data/home_prices.csv')  # We'll add this CSV next

# Features and target
X = df[['area']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'models/model.pkl')
print("Model saved to models/model.pkl")