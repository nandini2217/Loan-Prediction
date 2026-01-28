from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# ================= HOME =================
@app.route('/')
def home():
    return render_template("index.html")

# ================= PREDICT =================
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        return render_template("prediction.html")

    try:
        # ---------- INPUTS ----------
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        area = request.form['area']

        Credit_History = float(request.form['credit'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

        # ---------- VALIDATION ----------
        if ApplicantIncome <= 0 or LoanAmount <= 0 or Loan_Amount_Term <= 0:
            raise ValueError("Invalid numeric input")

        # ---------- ENCODING ----------
        Gender_Male = 1 if gender == "Male" else 0
        Married_Yes = 1 if married == "Yes" else 0
        Education_Not_Graduate = 1 if education == "Not Graduate" else 0
        Self_Employed_Yes = 1 if employed == "Yes" else 0

        Dependents_1 = Dependents_2 = Dependents_3_plus = 0
        if dependents == "1":
            Dependents_1 = 1
        elif dependents == "2":
            Dependents_2 = 1
        elif dependents == "3+":
            Dependents_3_plus = 1

        Property_Area_Semiurban = Property_Area_Urban = 0
        if area == "Semiurban":
            Property_Area_Semiurban = 1
        elif area == "Urban":
            Property_Area_Urban = 1

        # ---------- LOG FEATURES ----------
        ApplicantIncomeLog = np.log(ApplicantIncome)
        LoanAmountLog = np.log(LoanAmount)
        Loan_Amount_Term_Log = np.log(Loan_Amount_Term)
        Total_income_Log = np.log(ApplicantIncome + CoapplicantIncome)

        # ---------- FEATURE VECTOR (MATCH TRAINING) ----------
        features = [[
            Credit_History,
            ApplicantIncomeLog,
            LoanAmountLog,
            Loan_Amount_Term_Log,
            Total_income_Log,
            Gender_Male,
            Married_Yes,
            Education_Not_Graduate,
            Self_Employed_Yes,
            Property_Area_Semiurban,
            Property_Area_Urban,
            Dependents_1,
            Dependents_2,
            Dependents_3_plus
        ]]

        # ---------- PREDICTION ----------
        pred = model.predict(features)[0]
        prob = model.predict_proba(features)[0]

        approval_prob = round(prob[list(model.classes_).index(1)] * 100, 2)
        result = "Approved" if pred == 1 else "Rejected"

        return render_template(
            "prediction.html",
            prediction=result,
            probability=approval_prob
        )

    except Exception as e:
        return render_template(
            "prediction.html",
            error="Please enter valid inputs"
        )

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
