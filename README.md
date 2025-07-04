## techsophyTEST (Risk Assessment for New Policy Applications)
## Problem Statement: Create an automated underwriting system that evaluates insurance applications and determines acceptance, rejection, or additional information needs.
Skills Demonstrated:
*AI/ML: Implement risk scoring models, decision trees for underwriting rules, outlier detection*

Critical Thinking: 
*Understand underwriting principles, balance risk acceptance vs business growth, consider regulatory compliance*

Problem Solving: 
*Handle incomplete applications, conflicting information, edge cases in risk assessment*

Modular Structure:
*Separate application processing, risk evaluation, decision engine, and output generation*

Clear Architecture: 
*Flow from application data → risk scoring → underwriting rules → decision output → next steps*

Deliverable:
*Automated underwriting system that processes applications and provides decisions with reasoning.*
## PROPOSED SOLUTION
This project implements an automated underwriting pipeline with the following modular architecture:
# 1.ApplicationProcessor
Validates that required fields are present
Checks for conflicts (e.g., invalid age ranges)
# 2.RiskEvaluator
Uses a simple DecisionTreeClassifier (from scikit-learn) trained on sample data to estimate risk class
Maps risk class to a risk score between 0 and 1
# 3.DecisionEngine
Interprets the risk score according to defined thresholds
Makes an underwriting decision: Accept, Reject, or Additional Information Needed
# 4.OutputGenerator
Packages the decision and explanation for the applicant
# 5.AutomatedUnderwritingSystem
Coordinates the end-to-end flow: validation → risk scoring → decision → output

## PROJECT STRUCTURE
.TECHSOPHYTEST
├── riskAssessment.py
├── README.md

## Installation & Setup
1️⃣ Clone the repository:

bash

git clone https://github.com/yourusername/riskAssessment-system.git
cd riskAssessment-system

2️⃣ Set up your Python environment (recommended with venv):

bash

python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies:

bash
pip install scikit-learn numpy 

## Running the Underwriting System
Execute the Python file directly:

bash
python riskAssessment.py
It will process the hard-coded sample applications and print underwriting decisions along with the reasoning behind them, for example:

yaml

Application 1 Result: Accept
Reason: Low risk score (0.1)

Application 2 Result: Reject
Reason: High risk score (0.9)

Application 3 Result: Additional Information Needed
Reason: Moderate risk score (0.5)

## How It Works — Architecture Flow
flowchart TD
    A[Application Data] --> B[ApplicationProcessor]
    B --> C[RiskEvaluator]
    C --> D[DecisionEngine]
    D --> E[OutputGenerator]
    E --> F[Decision & Reasoning]
Step by Step:
*Validate: check required fields and reasonable ranges*
*Score: estimate risk using ML model*
*Decide: interpret risk score thresholds*
*Generate Output: produce human-readable result*
 
Contact
If you have questions, feel free to reach out!

Author: Divya A
Email: 22311a66e6@aiml.sreenidhi.edu.in
