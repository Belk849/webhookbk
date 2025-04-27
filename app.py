from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/sms', methods=['POST'])
def sms_reply():
    from_number = request.form.get('From')
    body = request.form.get('Body')

    if not from_number or not body:
        return jsonify({"error": "Missing From or Body"}), 400

    response = supabase.table('reponse').insert({
        'from_number': from_number,
        'reponse': body.strip()
    }).execute()

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)