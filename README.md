# Grocery Webapp

A modern, full-stack grocery management web application built with Flask (Python) and vanilla JavaScript. This application allows you to manage products, create orders, and track inventory with a clean, responsive UI.

##  Features

- **Product Management**: Add, edit, and delete products with units of measurement (UOM)
- **Order Management**: Create and view customer orders with multiple line items
- **UOM Management**: Add custom units of measurement (Kg, Litre, Piece, etc.)
- **Real-time Calculations**: Automatic total calculations for orders
- **Responsive UI**: Modern Bootstrap-based interface
- **SQLite Database**: Lightweight, file-based database (no external setup required)

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **UI Framework**: Bootstrap 5.3
- **Architecture**: RESTful API with static file serving

##  Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

##  Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/grocery-webapp.git
cd grocery-webapp
```

### 2. Set Up Virtual Environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m backend.app
```

### 5. Access the Application

Open your browser and navigate to: `http://127.0.0.1:5000`

## Project Structure

```
grocery-webapp/
├── backend/
│   ├── .venv/              # Virtual environment
│   ├── data/               # SQLite database files
│   ├── __init__.py         # Package initialization
│   ├── app.py              # Main Flask application
│   ├── db.py               # Database connection and initialization
│   ├── product_dao.py      # Product data access object
│   ├── order_dao.py        # Order data access object
│   ├── uom_dao.py          # Unit of measurement data access object
│   ├── requirements.txt    # Python dependencies
│   └── README_RUN.md       # Original run instructions
├── ui/
│   ├── assets/
│   │   ├── css/
│   │   │   └── styles.css  # Custom styles
│   │   └── js/
│   │       └── app.js      # Shared JavaScript functions
│   ├── index.html          # Home page
│   ├── products.html       # Product management page
│   ├── new_order.html      # Order creation page
│   └── orders.html         # Order listing page
├── .gitignore              # Git ignore rules
├── LICENSE                 # Project license
└── README.md               # This file
```



### Products
- `GET /api/products` - Get all products
- `POST /api/products` - Create a new product
- `PUT /api/products/<id>` - Update a product
- `DELETE /api/products/<id>` - Delete a product

### Orders
- `GET /api/orders` - Get all orders
- `GET /api/orders/<id>` - Get order details
- `POST /api/orders` - Create a new order

### Units of Measurement (UOM)
- `GET /api/uoms` - Get all UOMs
- `POST /api/uoms` - Create a new UOM

## Database Schema

The application uses SQLite with the following tables:

- **uoms**: Units of measurement (id, name)
- **products**: Product catalog (id, name, uom_id, price)
- **orders**: Customer orders (id, customer_name, total_amount, created_at)
- **order_items**: Order line items (id, order_id, product_id, quantity, price)

## Usage Guide

### Managing Products

1. Navigate to the **Products** page
2. Add new UOMs if needed (e.g., "Kg", "Litre", "Piece")
3. Add products with name, UOM, and price
4. Edit or delete existing products as needed

### Creating Orders

1. Go to the **New Order** page
2. Enter customer name
3. Add line items by selecting products and entering quantities
4. Prices are automatically calculated
5. Submit the order

### Viewing Orders

1. Visit the **Orders** page
2. View all orders with customer details and totals
3. Click "View" to see detailed line items

##  Security Notes

- This is a development application
- SQLite database is stored locally
- No authentication is implemented
- Use in production with proper security measures

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask framework
- UI powered by Bootstrap
- Icons from Bootstrap Icons
- Inspired by real-world grocery management needs

##  Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/grocery-webapp/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---

**Happy Coding! **
