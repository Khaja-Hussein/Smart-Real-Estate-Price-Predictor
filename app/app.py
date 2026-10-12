from flask import Flask, render_template, request
import joblib
from pathlib import Path
import pandas as pd

app = Flask(__name__)

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "house_price_model.pkl"
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            location = request.form["location"].strip()
            total_sqft = float(request.form["total_sqft"])
            bath = int(request.form["bath"])
            bhk = int(request.form["bhk"])

            if not location:
                raise ValueError("Please enter a location.")

            if total_sqft <= 0 or bath <= 0 or bhk <= 0:
                raise ValueError("All numeric values must be greater than zero.")

            input_data = pd.DataFrame([{
                "location": location,
                "total_sqft": total_sqft,
                "bath": bath,
                "bhk": bhk
            }])

            price = model.predict(input_data)[0]
            prediction = f"₹{price:.2f} lakhs"

        except ValueError as exc:
            error = str(exc)
        except Exception:
            error = "Unable to predict. Please check your inputs."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)