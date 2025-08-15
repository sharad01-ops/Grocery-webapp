from flask import Flask, request, jsonify, send_from_directory
import os

# Import package-local modules
from .db import init_db
from . import product_dao, uom_dao, order_dao

BASE_DIR = os.path.dirname(__file__)
UI_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "ui"))

app = Flask(
    __name__,
    static_folder=UI_DIR,
    static_url_path=""
)


def seed_minimum_data():
    # Ensure there are some default UOMs to make the UI usable immediately
    try:
        existing = uom_dao.get_all()
        if not existing:
            for name in ["Kg", "Litre", "Piece"]:
                uom_dao.insert_uom(name)
    except Exception:
        # Seeding is best-effort; do not block startup
        pass


def setup_database():
    init_db()
    seed_minimum_data()


# Static UI routes
@app.get("/")
def web_index():
    return send_from_directory(UI_DIR, "index.html")


# API routes
@app.get("/api/uoms")
def api_get_uoms():
    return jsonify(uom_dao.get_all())


@app.post("/api/uoms")
def api_add_uom():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400
    uid = uom_dao.insert_uom(name)
    return jsonify({"id": uid, "name": name}), 201


@app.get("/api/products")
def api_get_products():
    return jsonify(product_dao.get_all())


@app.post("/api/products")
def api_add_product():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    uom_id = data.get("uom_id")
    price = float(data.get("price") or 0)
    if not name or not uom_id:
        return jsonify({"error": "name and uom_id are required"}), 400
    pid = product_dao.insert_product(name, int(uom_id), price)
    return jsonify({"id": pid}), 201


@app.put("/api/products/<int:product_id>")
def api_update_product(product_id: int):
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    uom_id = data.get("uom_id")
    price = float(data.get("price") or 0)
    if not name or not uom_id:
        return jsonify({"error": "name and uom_id are required"}), 400
    ok = product_dao.update_product(product_id, name, int(uom_id), price)
    if not ok:
        return jsonify({"error": "not found"}), 404
    return jsonify({"updated": True})


@app.delete("/api/products/<int:product_id>")
def api_delete_product(product_id: int):
    ok = product_dao.delete_product(product_id)
    if not ok:
        return jsonify({"error": "not found"}), 404
    return jsonify({"deleted": True})


@app.get("/api/orders")
def api_get_orders():
    return jsonify(order_dao.get_all())


@app.get("/api/orders/<int:order_id>")
def api_get_order(order_id: int):
    order = order_dao.get_order_with_items(order_id)
    if not order:
        return jsonify({"error": "not found"}), 404
    return jsonify(order)


@app.post("/api/orders")
def api_create_order():
    data = request.get_json(silent=True) or {}
    if not data.get("customer_name") or not data.get("items"):
        return jsonify({"error": "customer_name and items are required"}), 400
    oid = order_dao.insert_order(data)
    return jsonify({"id": oid}), 201


def main():
    setup_database()
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
