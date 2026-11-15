from flask import Flask, render_template

from database import get_products

from database import get_sales

from database import get_stock

app=Flask(__name__)

@app.route('/')
def home():
    index_data=get_index()
    return render_template('index.html', l=index_data)

@app.route('/products')
def products():
    products_data=get_products()
    return render_template('products.html',x =products_data)

@app.route('/sales')
def sales():
    sales_data=get_sales()
    return render_template('sales.html',x=sales_data)

@app.route('/stock')
def stock():
    stock_data=get_stock()
    return render_template('stock.html', y=stock_data)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    login_data=get_login()
    return render_template('login.html', k=login_data)


app.run(debug=True)