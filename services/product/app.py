from flask import Flask, jsonify, request

app = Flask(__name__)

# Example endpoint for product information
@app.route('/product', methods=['GET'])
def get_product():
    product_id = request.args.get('product_id')
    
    # Example data (replace this with a database lookup)
    products = {
        "1": {"name": "Laptop", "price": 1200},
        "2": {"name": "Phone", "price": 800}
    }
    
    product = products.get(product_id)
    
    if product:
        return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
