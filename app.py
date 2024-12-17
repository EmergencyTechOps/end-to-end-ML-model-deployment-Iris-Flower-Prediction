from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Load model
model = joblib.load("iris_model.pkl")

# Initialize app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
