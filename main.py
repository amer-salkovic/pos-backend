import psycopg

def get_products(cur):
    cur.execute("SELECT name, price, stock FROM products")
    products = cur.fetchall()
    return products

def get_low_stock_products(cur):
    cur.execute("SELECT name, price, stock FROM products WHERE stock < 20")
    products = cur.fetchall()
    return products

def search_products(cur, search_term):
    pattern = f"%{search_term}%"

    cur.execute(
        "SELECT name, price, stock FROM products WHERE name ILIKE %s",
        (pattern,)
    )

    products = cur.fetchall()
    return products

conn = psycopg.connect(dbname="pos_system")
cur = conn.cursor()



while True:
    search_term = input("Unesi proizvod (exit za izlaz): ")

    if search_term == "exit":
        break
    
    
    products = search_products(cur, search_term)

    if not products:
        print("Nema proizvoda sa tim imenom.")
    
    
    else:

     for product in products:
        name, price, stock = product
        print(f"{name} | {price} RSD | {stock} komada")





cur.close()
conn.close()