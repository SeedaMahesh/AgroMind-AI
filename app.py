from flask import Flask, request, jsonify
from flask_cors import CORS

from cnn.predict_disease import predict_disease

app = Flask(__name__)

CORS(app)


# Home Route
@app.route("/")
def home():

    return "AgroMind AI Backend Running"


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    # Check image exists
    if "image" not in request.files:

        return jsonify({

            "error": "No image uploaded"

        })


    # Get image
    image = request.files["image"]

    # Save temporarily
    image_path = "temp.jpg"

    image.save(image_path)


    # CNN Prediction
    disease, confidence = predict_disease(image_path)


    # Dummy Weather Prediction
    temperature = 31.9

    rainfall = 0.4

    wind = 12.3


    # Dummy Risk Logic
    if rainfall > 5:

        risk = "HIGH"

        message = "High moisture may spread disease rapidly."

    else:

        risk = "LOW"

        message = "Current conditions are relatively safe."


    # Final Response
    result = {

        "disease": disease,

        "confidence": confidence,

        "temperature": temperature,

        "rainfall": rainfall,

        "wind": wind,

        "risk": risk,

        "message": message
    }


    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True)