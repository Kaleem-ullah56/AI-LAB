from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model + scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # MUST BE EXACTLY 13 FEATURES (ORDER MATTERS!)
        features = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["fbs"]),
            float(request.form["restecg"]),
            float(request.form["thalach"]),
            float(request.form["exang"]),
            float(request.form["oldpeak"]),
            float(request.form["slope"]),
            float(request.form["ca"]),
            float(request.form["thal"])
        ]

        print("Input length:", len(features))  # DEBUG

        final_features = np.array([features])
        scaled = scaler.transform(final_features)
        prediction = model.predict(scaled)[0]

        if prediction == 1:
            result = "⚠ High Risk of Heart Disease"
        else:
            result = "✅ Low Risk of Heart Disease"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)