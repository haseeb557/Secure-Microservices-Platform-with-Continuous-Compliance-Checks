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

# New endpoint for displaying Product service information
@app.route('/product_info', methods=['GET'])  # Change the route to '/product_info'
def product_info():
    return """
    <html>
        <head><title>Product Service</title></head>
        <body>
            <h2>Product Service</h2>
            <p>Use GET <code>/product</code> with query parameter <code>product_id</code> to get product details.</p>
            <h3>Example:</h3>
            <pre>
GET /product?product_id=1
            </pre>
            <p>Example response:</p>
            <pre>
{
    "name": "Laptop",
    "price": 1200
}
            </pre>
        </body>
    </html>
    """

# Make sure Flask can find the app when using 'flask run'
application = app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)  # Port 5002 for product service

#http://localhost:5002/product_info 