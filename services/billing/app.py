from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint for billing
@app.route('/bill', methods=['POST'])
def bill():
    data = request.get_json()
    customer_id = data.get('customer_id')
    amount = data.get('amount')
    
    if customer_id and amount:
        return jsonify({"message": f"Bill for customer {customer_id} is ${amount}"}), 200
    return jsonify({"message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
