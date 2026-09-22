
products = [
    {"id": 101, "name": "Keyboard", "price": 150.00, "stock": 5},
    {"id": 102, "name": "Mouse", "price": 80.00, "stock": 8},
    {"id": 103, "name": "Monitor", "price": 1200.00, "stock": 3},
    {"id": 104, "name": "Headset", "price": 250.00, "stock": 6}
]

print("1 - List products")
print("2 - Create order")
print("3 - Cancel order")
print("4 - Show orders")
print("5 - Sales report")
print("0 - Exit")

option = input("Choose a option: ").strip().lower()
option = option.replace(" ","")

if option in ("1","1-listproducts"):
    for i in range(len(products)):
        print(products[i])

elif option in ("2","2-createorder"):

    orderclient = []

    while True:
        idorder = input("inform the product ID: ").strip()

        if not idorder.isdigit():
            print("Insert only positive inteer numbers")
            continue
        
        
        idorder = int(idorder)

        found = False
        found_product = None
        for product in products:

            if product["id"] == idorder:
                found = True
                found_product = product
                break


        if not found:
            print("Product not found, try again...")
            continue
        
        print(f"Product found, ({found_product['name']})")

        while True:

            stockorder = input("Inform the quantity of product: ").strip()

            if not stockorder.isdigit():
                print("Insert only positive inteer numbers")
                continue

            stockorder = int(stockorder)
        
            if stockorder > found_product['stock']:
                print(f"Sorry, but we have only {found_product['stock']} unitys in stock. Please try again")
                continue

            elif stockorder == 0:
                print("Insert a quanty greater than zero...")
                continue

            else:
                print("Sucess!")
                print(f"{stockorder} unitys of {found_product['name']} went into your cart")
                break

        order = {"id": idorder, "name": found_product["name"],"price": found_product["price"], "quantity": stockorder }
        orderclient.append(order)

        again = input("You want to continue? Yes/No: ").strip().lower()

        while again not in ("yes","y","no","n"):
            print("Insert 'Yes' to add a new product in your order or 'not' for exit") 
            again = input("You want to continue? Yes/No: ").strip().lower()
             
        if again in ("yes","y"):
            continue
        
        elif again in ("no","n"):
            print(f"Your order: {orderclient}")
            while True:

                confirm = input("Do you confirm your order? Yes/No: ").strip().lower()
                if confirm not in ("yes","y","no","n"):
                    print("Insert 'Yes' to confirm the order or 'not' for cancel the order")

                    continue

                elif confirm in ("yes","y"):
                    print("Order successfully generated!")

                    for product1 in products:
                        for product2 in orderclient:
                            if product2["id"] == product1["id"]:
                                newstock = product1["stock"] - product2["quantity"] 
                                product1["quantity"] = newstock
                                break

                    print(products)
                        
                    break

                else:
                    del orderclient
                    print("Order successfully cancelled!")
                    break
            break

                                   







