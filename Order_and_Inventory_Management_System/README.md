# Order and Inventory Management System

A Python project developed to practice logic, data structures, functions, input validation, and inventory management.

## Features

* List available products
* Create orders with multiple products
* Validate product IDs and quantities
* Prevent orders with insufficient stock
* Update inventory after a confirmed order
* Cancel orders
* Restore stock after an order cancellation
* Keep cancelled orders in the order history
* Generate a sales report
* Handle invalid user input without crashing

## Concepts Practiced

This project uses:

* Python functions
* Lists
* Dictionaries
* `for` and `while` loops
* Conditional statements
* Input validation
* `enumerate()`
* Data manipulation
* Basic inventory logic

## Example Product Structure

```python
products = [
    {"id": 101, "name": "Keyboard", "price": 150.00, "stock": 5},
    {"id": 102, "name": "Mouse", "price": 80.00, "stock": 8}
]
```

## Menu

```text
1 - List products
2 - Create order
3 - Cancel order
4 - Show orders
5 - Sales report
0 - Exit
```

## Main Challenge

One of the main challenges of this project is keeping the inventory consistent.

If one product in an order does not have enough stock, the entire order must be rejected without changing the inventory.

When an order is cancelled, all products from that order must be returned to stock.

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project folder:

```bash
cd Order_and_Inventory_Management_System
```

Run the program:

```bash
python3 Order_and_inventary_system.py
```

## Status

Project under development.

## Author

Gustavo Sanches
