# ai_model/classifier/rules.py
class FraudDetector:
    @staticmethod
    def rule_based_checks(data):
        flags = []
        
        # Rule 1: Amount threshold [[10]]
        if data.get("claim_amount", 0) > 100000:
            flags.append("EXCESSIVE_AMOUNT")
            
        # Rule 2: Date validity
        if not data.get("date_of_service"):
            flags.append("MISSING_DATE")
            
        return len(flags) == 0, flags

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