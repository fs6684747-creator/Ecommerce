from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Smart Phone",
        "price": 15000,
        "image": "phone.jpg",
        "description": "Latest smartphone with high performance."
    },
    {
        "id": 2,
        "name": "Laptop",
        "price": 55000,
        "image": "laptop.jpg",
        "description": "Powerful laptop for work and study."
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2500,
        "image": "headphones.jpg",
        "description": "Noise cancelling headphones."
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 4000,
        "image": "smartwatch.jpg",
        "description": "Track fitness and notifications."
    },
    {
        "id": 5,
        "name": "Camera",
        "price": 30000,
        "image": "camera.jpg",
        "description": "High quality digital camera."
    },
    {
        "id": 6,
        "name": "Shoes",
        "price": 3500,
        "image": "shoes.jpg",
        "description": "Comfortable sports shoes."
    }
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    item = next(p for p in products if p["id"] == product_id)
    return render_template("product.html", product=item)

if __name__ == "__main__":
    app.run(debug=True)
