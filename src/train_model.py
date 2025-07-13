import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
df = pd.read_csv('data/phishing.csv')

# Drop 'Index' column if it exists
if 'Index' in df.columns:
    df.drop('Index', axis=1, inplace=True)

# ✅ Correct label column name is 'class' (small 'c')
X = df.drop('class', axis=1)
y = df['class'] 

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/phishing_model.pkl')

print("✅ Model trained and saved successfully!")
