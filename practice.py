import json
products = [{"name": "Laptop", "price": 800, "stock": 5}, {"name": "Mouse", "price": 20, "stock":10},{"name": "Keyboard", "price": 40, "stock": 7}]
orders = []
def save_products():
    with open("products.json", "w") as file:
        json.dump(products, file)
def load_products():
    global products
    try:
        with open("products.json", "r") as file:
            products = json.load(file)
    except FileNotFoundError:
        save_products()
def save_orders():
    with open("orders.json", "w") as file:
        json.dump(orders, file)
def load_orders():
    global orders
    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        save_orders()                                     
def show_products():
    for product in products:
        print(f"Name: {product['name']} | "
              f"Price:{product['price']} | "
              f"stock:{product['stock']}")
def add_product():
    name = input("Product name: ")
    price = float(input("Product price: "))
    stock = int(input("Product stock: "))
    product = {"name": name, 
               "price": price,
               "stock": stock}
    products.append(product)
    save_products()
def search_product():
    name = input("Product name: ")
    for product in products:
        if product["name"].lower() == name.lower():
            print(product) 
            return
    print("Product not found")
def delete_product():
    name = input("Product name: ")
    for product in products:
        if product["name"].lower() == name.lower():
           products.remove(product)
           save_products()
           print("Product deleted successfully!")
           return
    print("Product not found")
def create_order():
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    for product in products:
        if product["name"].lower() == name.lower():
            print("Product found:")
            print(product)
            if quantity > product["stock"]:
                print("Not enough stock")
                return
            total = product["price"] * quantity
            print(f"Total price: {total}")
            product["stock"] -= quantity
            order = {"name": product["name"],
                      "quantity": quantity,
                        "total": total}
            orders.append(order)
            save_products()
            save_orders()
            return
    print("Product not found")
def show_orders():
    if not orders:
        print("No orders found")
        return
    for order in orders:
        print(f"Product: {order['name']} | "
              f"Quality: {order['quantity']} | "
              f"Total: {order['total']}")
def calculate_orders_total() :
    total = 0
    for order in orders:
        total += order["total"] 
    print(f"All orders total: {total}")
load_products()
load_orders()    
while True:
    print("1. Show products") 
    print("2. Creat order")
    print("3. Show orders")
    print("4. Show total") 
    print("5. Exit")
    print("6. Add product")
    print("7. Search product")
    print("8. Delete product")
    choice = input("Choose an option: ") 
    if choice == "1":
        show_products()
    elif choice == "2":
        create_order()
    elif choice == "3":
        show_orders()
    elif choice == "4" :
        calculate_orders_total()
    elif choice == "6":
        add_product()
    elif choice == "7":
        search_product()
    elif choice == "8":
        delete_product()                      
    elif choice == "5":   
        print("Goodbye!")
        break 
    else:
        print("Invalid choice") 

       

        