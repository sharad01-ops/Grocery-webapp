from .db import get_connection

def insert_order(data):
    conn = get_connection()
    cur = conn.cursor()
    total = float(data.get('total_amount', 0) or 0)
    cur.execute("INSERT INTO orders(customer_name, total_amount) VALUES(?,?)",
                (data.get('customer_name'), total))
    order_id = cur.lastrowid

    for item in data.get('items', []):
        cur.execute(
            """
            INSERT INTO order_items(order_id, product_id, quantity, price)
            VALUES(?,?,?,?)
            """,
            (order_id, item['product_id'], item['qty'], item['price'])
        )
    conn.commit()
    conn.close()
    return order_id

def get_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT id, customer_name, total_amount, created_at
                   FROM orders ORDER BY id DESC""")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def get_order_with_items(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT id, customer_name, total_amount, created_at
                   FROM orders WHERE id=?""", (order_id,))
    order = cur.fetchone()
    if not order:
        conn.close()
        return None
    order = dict(order)
    cur.execute("""SELECT oi.id, oi.quantity, oi.price,
                          p.name as product_name, p.uom_id
                   FROM order_items oi
                   JOIN products p ON p.id = oi.product_id
                   WHERE oi.order_id=?""", (order_id,))
    items = [dict(r) for r in cur.fetchall()]
    conn.close()
    order['items'] = items
    return order
