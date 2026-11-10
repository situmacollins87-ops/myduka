from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/products')
def products():
    return "products page"

@app.route('/sales')
def sales():
    return "sales page"

@app.route('/stock')
def stock():
    return "stock page"

@app.route('/dashboard')
def dashboard():
    return "dashboard page"

@app.route('/register')
def register():
    return "register page"

@app.route('/login')
def login():
    return "login page"


app.run(debug=True)