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
        
        else:
            idorder = int(idorder)

        found = False

        for product in products:

            if product["id"] == idorder:
                found = True


        if not found:
            print("Product not found, try again...")

        else:
            print(f"Product found")
            stockorder = input("Inform the quantity of product: ").strip()

            if not stockorder.isdigit():
                print("Insert only positive inteer numbers")

            else:
                stockorder = int(stockorder)
                indexid = 0

                for index, product in enumerate(products):
                    if product["id"] == idorder:
                        indexid = index

                if stockorder > products[indexid]["stock"]:
                    print(f"Sorry, but we have only {products[indexid]['stock']} unitys in stock. Please try again")

                else:
                    print("Sucess!")
                    orderclient['id'] = idorder
                    orderclient['unity'] = stockorder

                    again = input("You want to continue?: ").strip().lower()
                    if again in ("no","n"):

                        print(orderclient)
                         
                        break








