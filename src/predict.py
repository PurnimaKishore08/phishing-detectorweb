import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/phishing_model.pkl')

# Sample input for one prediction (Replace this with 29 actual values)
sample_input = np.array([[1, -1, 0, 1, 0, -1, 1, 1, 1, 1, 0, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 0, 1, 1, 1, 0, 1, 1, -1]])

# Predict
prediction = model.predict(sample_input)

# Print output
if prediction[0] == 1:
    print("✅ This website is Legitimate.")
else:
    print("🚨 Warning: This website is Phishing.")
