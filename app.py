from flask import Flask, render_template, request
import joblib





app = Flask(__name__)

# Load your trained model
modell = joblib.load("/Users/arnoldsomuah/Downloads/Final_Credit Scoring/venv/credit_scoring_model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input values from the form
        input_data = get_input_data(request.form)

        # Make a prediction using the model
        prediction = modell.predict(input_data.reshape(1, -1))

        # Return the prediction result
        return render_template('index.html', prediction=prediction[0])
    return render_template('index.html')

def get_input_data(form_data):
    # Extract and preprocess input data from the form
    age = int(form_data['age'])
    income = int(form_data['income'])
    credit_score = int(form_data['credit_score'])
    loan_amount = int(form_data['loan_amount'])
    loan_term = int(form_data['loan_term'])
    employment_status = form_data['employment_status']
    housing_status = form_data['housing_status']

    # One-hot encode categorical variables
    if employment_status == 'employed':
        employed = 1
        self_employed = 0
        unemployed = 0
    elif employment_status == 'self_employed':
        employed = 0
        self_employed = 1
        unemployed = 0
    else:
        employed = 0
        self_employed = 0
        unemployed = 1

    if housing_status == 'own':
        own = 1
        rent = 0
        mortgage = 0
    elif housing_status == 'rent':
        own = 0
        rent = 1
        mortgage = 0
    else:
        own = 0
        rent = 0
        mortgage = 1

    # Create input array for the model
    input_data = [age, income, credit_score, loan_amount, loan_term, employed, self_employed, unemployed, own, rent, mortgage]

    return input_data

if __name__ == '__main__':
    app.run(debug=True)
