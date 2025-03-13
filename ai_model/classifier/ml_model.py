# ai_model/classifier/ml_model.py (Example with synthetic data)
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class MLClassifier:
    def __init__(self):
        self.model = RandomForestClassifier()
        # Dummy training data
        X_train = np.array([[5000.00, 1], [120000.00, 0]])
        y_train = np.array([1, 0])  # 1=Valid, 0=Fraudulent
        self.model.fit(X_train, y_train)
        
    def predict(self, amount, diagnosis_code):
        return self.model.predict([[amount, diagnosis_code]])[0]