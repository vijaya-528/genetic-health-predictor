from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy family tree data (later connect to DB)
family_tree = {
    "name": "John",
    "children": [
        {"name": "Alice", "disease": "Diabetes"},
        {"name": "Bob", "disease": "Healthy"}
    ]
}

# --- Routes ---

@app.route("/")
def home():
    return {"message": "Genetic Health Predictor API is running 🚀"}

# Get family tree (placeholder)
@app.route("/family-tree", methods=["GET"])
def get_family_tree():
    return jsonify(family_tree)

# Predict health risk (dummy ML model for now)
@app.route("/predict", methods=["POST"])
def predict_risk():
    data = request.json
    # Example input: {"name": "Alice", "age": 30, "disease_history": ["Diabetes"]}
    
    # Dummy logic (replace with ML later)
    risk_score = 0.8 if "Diabetes" in data.get("disease_history", []) else 0.3
    
    return jsonify({
        "name": data.get("name"),
        "risk_score": risk_score,
        "recommendation": "Regular checkup advised" if risk_score > 0.5 else "Low risk"
    })

if __name__ == "__main__":
    app.run(debug=True)
