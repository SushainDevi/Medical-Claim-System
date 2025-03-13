from ai_model.classifier.rules import FraudDetector

def test_amount_threshold():
    data = {"claim_amount": 120000}
    is_valid, flags = FraudDetector.rule_based_checks(data)
    assert not is_valid
    assert "EXCESSIVE_AMOUNT" in flags