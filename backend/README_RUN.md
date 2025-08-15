# Grocery Webapp (Executable, SQLite)

This package is a ready-to-run version of the Codebasics grocery webapp (with essential enhancements) adapted to **SQLite** so it runs without any external DB setup.

## What's included

- Product **Edit** (PUT) + Delete
- **Add UOM** (POST) + UI helper
- Order form **validations** (customer, item name, qty, price)
- **Grand total** recalculation fix
- Orders **View Details** modal

## How to run

1. Create a virtual environment (optional but recommended):
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python -m app
   ```

4. Open the UI:
   - Visit http://localhost:5000 in your browser.
   - Use the navigation links to go to Products, New Order, Orders.

> The SQLite database file is created at `backend/data/grocery.db` on first run.

## Notes

- If you want to port this back to MySQL, you can replace `backend/db.py` with a connector to MySQL and keep the DAOs the same structure (adjust placeholders and syntax accordingly).
