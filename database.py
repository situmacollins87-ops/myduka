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





