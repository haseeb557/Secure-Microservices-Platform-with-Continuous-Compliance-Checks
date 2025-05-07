from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/bill', methods=['POST'])
def bill():
    data = request.get_json()
    customer_id = data.get('customer_id')
    amount = data.get('amount')
    
    if customer_id and amount:
        return jsonify({"message": f"Bill for customer {customer_id} is ${amount}"}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/bill_info', methods=['GET'])
def bill_info():
    return """
    <html>
        <head><title>Billing Info</title></head>
        <body>
            <h2>Billing Service</h2>
            <p>Use POST <code>/bill</code> with JSON data to get billing info.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Port 5001 for billing service

#Billing info page available at: http://localhost:5001/bill_info"