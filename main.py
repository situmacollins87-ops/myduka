from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_products, fetch_sales, insert_products, insert_sales, get_profit_per_day, get_profit_per_product, get_sales_per_day, get_sales_per_product


app = Flask(__name__)

app.secret_key='terry'


@app.route('/') 
def home(): 
    name = "Jane"
    return render_template('index.html',)



@app.route('/products')
def products():
    products_data = get_products()
    return render_template('products.html',products_data = products_data)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == "POST":
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price'] 

        new_product=(product_name,buying_price,selling_price)
        insert_products(new_product)
        flash("products added successfuly",'success')
    return redirect(url_for('products'))


@app.route('/sales')
def sales():
    sales_data = fetch_sales()
    return render_template('sales.html', sales_data=sales_data)

@app.route('/add_sales', methods=['GET', 'POST'])
def add_sales():
    if request.method == "POST":
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = ( pid, quantity)
        insert_sales(new_sale)
        print("Sales added successfully")
    return redirect(url_for('sales'))




@app.route('/stock')
def stock():
    return render_template('stock.html')



@app.route('/dashboard')
def dashboard():

    product_sales=get_sales_per_product()
    daily_sales=get_sales_per_day()
    product_profit=get_profit_per_product()
    daily_profit=get_profit_per_day()

    product_names = [i[0] for i in product_sales]
    sales_p = [ float(i[1]) for i in product_sales]
    profit_p = [float(i[1]) for i in product_profit]


    days = [ str(i[0]) for i in daily_sales ]
    sales_day = [ float(i[1]) for i in daily_sales ]
    profit_day = [ float(i[1]) for i in daily_profit ]
    return render_template('dashboard.html',
    product_names=product_names,sales_p=sales_p, profit_p=profit_p,
    days=days, sales_day=sales_day,profit_day=profit_day)

             



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/login')
def login():
    return render_template('login.html')




app.run(debug=True)