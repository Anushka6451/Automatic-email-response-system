# Load trained model
import os
import joblib

# Get current file directory
BASE_DIR = os.path.dirname(__file__)

# Correct path to model
model_path = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(model_path)

def predict_category(email_text):
    return model.predict([email_text])[0]


# Test
if __name__ == "__main__":
    test_email = "I want refund"
    print("Predicted:", predict_category(test_email))