from .db import get_connection

def get_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM uoms ORDER BY name")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows

def insert_uom(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO uoms(name) VALUES(?)", (name,))
    conn.commit()
    uid = cur.lastrowid
    conn.close()
    return uid
