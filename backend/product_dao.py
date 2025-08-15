from .db import get_connection

def get_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.id, p.name, p.price, u.name as uom_name, u.id as uom_id
        FROM products p JOIN uoms u ON p.uom_id = u.id
        ORDER BY p.id DESC
    """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def insert_product(name, uom_id, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name, uom_id, price) VALUES(?,?,?)",
                (name, uom_id, price))
    conn.commit()
    pid = cur.lastrowid
    conn.close()
    return pid

def update_product(product_id, name, uom_id, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE products SET name=?, uom_id=?, price=? WHERE id=?",
                (name, uom_id, price, product_id))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok

def delete_product(product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    ok = cur.rowcount > 0
    conn.close()
    return ok
