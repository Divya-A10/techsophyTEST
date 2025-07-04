from sklearn.tree import DecisionTreeClassifier
import numpy as np

class ApplicationProcessor:
    REQUIRED_FIELDS = ['age', 'smoker', 'chronic_illness']

    def validate(self, application):
        missing = [f for f in self.REQUIRED_FIELDS if f not in application]
        if missing:
            return False, f"Missing required fields: {missing}"
        return True, None

    def handle_conflicts(self, application):
        if not (18 <= application['age'] <= 100):
            return False, "Age out of allowed range (18-100)."
        return True, None


class RiskEvaluator:
    def __init__(self):
        self.clf = DecisionTreeClassifier()
        X = np.array([
            [25, 0, 0],  # low risk
            [45, 1, 0],  # medium risk
            [60, 1, 1],  # high risk
            [35, 0, 1],  # medium-high risk
        ])
        y = np.array([0, 1, 2, 2])  
        self.clf.fit(X, y)

        self.risk_score_map = {0: 0.1, 1: 0.5, 2: 0.9} 

    def score(self, application):
     
        age = application['age']
        smoker = 1 if application['smoker'] else 0
        chronic = 1 if application['chronic_illness'] else 0

        pred_class = self.clf.predict([[age, smoker, chronic]])[0]
        risk_score = self.risk_score_map[pred_class]
        return risk_score

class DecisionEngine:
    def __init__(self):
        self.accept_threshold = 0.3
        self.reject_threshold = 0.7

    def decide(self, risk_score):
        if risk_score <= self.accept_threshold:
            return "Accept", f"Low risk score ({risk_score})"
        elif risk_score >= self.reject_threshold:
            return "Reject", f"High risk score ({risk_score})"
        else:
            return "Additional Information Needed", f"Moderate risk score ({risk_score})"


class OutputGenerator:
    def generate(self, decision, reason):
        return {
            "decision": decision,
            "reason": reason
        }


class AutomatedUnderwritingSystem:
    def __init__(self):
        self.processor = ApplicationProcessor()
        self.evaluator = RiskEvaluator()
        self.engine = DecisionEngine()
        self.output_gen = OutputGenerator()

    def process_application(self, application):
        # Validate application data
        valid, msg = self.processor.validate(application)
        if not valid:
            return self.output_gen.generate("Additional Information Needed", msg)

        # Check for conflicts/outliers
        valid, msg = self.processor.handle_conflicts(application)
        if not valid:
            return self.output_gen.generate("Reject", msg)

        # Evaluate risk score
        risk_score = self.evaluator.score(application)

        # Make decision based on risk score
        decision, reason = self.engine.decide(risk_score)

        # Generate output
        return self.output_gen.generate(decision, reason)


if __name__ == "__main__":
    system = AutomatedUnderwritingSystem()

    # Example applications
    applications = [
        {"age": 30, "smoker": False, "chronic_illness": False},  # Low risk, Accept
        {"age": 50, "smoker": True, "chronic_illness": True},    # High risk, Reject
        {"age": 40, "smoker": True, "chronic_illness": False},   # Moderate risk, Additional Info
        {"age": 17, "smoker": False, "chronic_illness": False},  # Age out of range, Reject
        {"age": 45, "smoker": False},                            # Missing chronic_illness, Additional Info
    ]

    for i, app in enumerate(applications, 1):
        result = system.process_application(app)
        print(f"Application {i} Result: {result['decision']}\nReason: {result['reason']}\n")
