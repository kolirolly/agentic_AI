from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import requests
import os

app = Flask(__name__)

# Load local doctors.csv
doctors_df = pd.read_csv('doctors.csv')

GROQ_API_KEY = "your_api_code"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


@app.route('/')
def home():
    # serve index.html from the same folder
    return send_from_directory(os.getcwd(), 'index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        symptom = data.get("symptom", "").strip()

        if not symptom:
            return jsonify({"error": "No symptom provided"}), 400

        # Send request to Groq
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a medical assistant that summarizes medical protocols safely. Never give direct diagnoses. Always advise consulting a doctor."
                },
                {
                    "role": "user",
                    "content": f"Summarize the medical protocol for the symptom: {symptom}. "
                               "Include: possible causes, risk level, and care guidelines. "
                               "Use concise bullet points."
                }
            ],
            "max_tokens": 400,
            "temperature": 0.3
        }

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(GROQ_URL, headers=headers, json=payload)
        groq_data = response.json()
        summary_text = groq_data["choices"][0]["message"]["content"]

        # Determine risk
        if any(word in summary_text.lower() for word in ["emergency", "severe", "critical", "urgent"]):
            risk_level = "High-Risk: Immediate medical attention recommended."
        else:
            risk_level = "Standard Care: Schedule a consultation with a healthcare provider."

        # Fetch nearby doctors (simple subset)
        doctors_list = doctors_df.sample(min(2, len(doctors_df)))[["name", "address", "specialty", "phone_number"]].to_dict(orient="records")

        return jsonify({
            "summary": summary_text,
            "risk": risk_level,
            "doctors": doctors_list
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
