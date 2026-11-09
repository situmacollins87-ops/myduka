import psycopg2
conn=psycopg2.connect(host='localhost',port=5433,user= 'postgres' ,password='Jimmax87',dbname='myduka_db')
#creating a cur object to perform db operations
cur=conn.cursor()
cur.execute("select * from products")
products_data=cur.fetchall()
print(products_data)
def get_products():
    cur.execute("select * from products")
    products_data=cur.fetchall()
    return products_data
products_data=get_products()
print(products_data)

def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('assus laptop',40000,50000)")
    conn.commit()
insert_products()
products_data=get_products()
print(products_data)



cur=conn.cursor()
cur.execute("select * from sales")
sales_data=cur.fetchall()
print(sales_data)
def get_sales():
    cur.execute("select * from sales")
    sales_data=cur.fetchall()
    return sales_data
sales_data=get_sales()
print(sales_data)

def insert_sales():
    cur.execute("insert into sales (pid, quantity, created_at) values (3, 45, NOW());")
    conn.commit()
insert_sales()
sales_data=get_sales()
print(sales_data)

def fetch_sales():
    cur.execute("select * from sales")
    sales_data=cur.fetchall()
    return sales_data

def insert_sales(sale_details):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sale_details)
    conn.commit()

sale1=(3,45)
sale2=(4,2)
insert_sales(sale1)
insert_sales(sale2)

sales_data=fetch_sales()
print(sales_data)


def fetch_products():
    cur.execute("select * from products")
    products_data=cur.fetchall()
    return products_data

def insert_products(products_details):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",products_details)
    conn.commit()

product1=('iphone 14',44000,53000)
product2=('rice',200,600)
insert_products(product1)
insert_products(product2)

products_data=get_products()
print(products_data)

#I experienced difficulties on a general function that can insert any stock. Am open for guidance.

cur=conn.cursor()
cur.execute("select * from stock")
stock_data=cur.fetchall()
print(stock_data)
def get_stock():
    cur.execute("select * from stock")
    stock_data=cur.fetchall()
    return stock_data
stock_data=get_sales()
print(stock_data)


def get_sales_per_day():
    cur.execute("""
        SELECT
            DATE(sales.created_at) AS sale_day,
            SUM(products.selling_price * sales.quantity) AS total_sales FROM sales JOIN products ON products.id = sales.pid GROUP BY sale_day ORDER BY sale_day;
    """)

    sales_per_day = cur.fetchall()
    return sales_per_day

sales_per_day = get_sales_per_day()
print(sales_per_day)


def get_profit_per_product():
    cur.execute("""
        SELECT
            products.name AS p_name,
            SUM((products.selling_price - products.buying_price) * sales.quantity) AS total_profit
        FROM sales
        JOIN products ON products.id = sales.pid
        GROUP BY products.id, products.name
        ORDER BY total_profit DESC;
    """)

    profit_per_product=cur.fetchall()
    return profit_per_product

profit_per_product=get_profit_per_product()
print(profit_per_product)



def get_profit_per_day():
     cur.execute("""   
     SELECT
            DATE(sales.created_at) AS sale_day,SUM((products.selling_price - products.buying_price)* sales.quantity) AS total_profit FROM sales 
            JOIN products ON products.id = sales.pid GROUP BY sale_day ORDER BY sale_day;
""")

     profit_per_day=cur.fetchall()
     return profit_per_day

profit_per_day=get_profit_per_day()
print(profit_per_day)







