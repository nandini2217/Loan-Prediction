from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # collect inputs
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

        # encoding
        male = 1 if gender == "Male" else 0
        married_yes = 1 if married == "Yes" else 0
        not_graduate = 1 if education == "Not Graduate" else 0
        employed_yes = 1 if employed == "Yes" else 0

        dependents_1 = dependents_2 = dependents_3 = 0
        if dependents == '1':
            dependents_1 = 1
        elif dependents == '2':
            dependents_2 = 1
        elif dependents == '3+':
            dependents_3 = 1

        semiurban = urban = 0
        if area == "Semiurban":
            semiurban = 1
        elif area == "Urban":
            urban = 1

        # logs
        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome + CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)

        prediction = model.predict([[
            credit, ApplicantIncomelog, LoanAmountlog,
            Loan_Amount_Termlog, totalincomelog,
            male, married_yes, dependents_1, dependents_2,
            dependents_3, not_graduate, employed_yes,
            semiurban, urban
        ]])[0]

        prediction = "Yes" if prediction == 'Y' else "No"

        return render_template(
            "prediction.html",
            prediction_text=f"Loan status is {prediction}"
        )

    return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
