def create_order(products,showorders):
    # Stores the products from the current order
    orderclient = []
    # The order status starts disabled
    orderstatus = "Disabled"


    # Main loop to create the order
    while True:

        # Ask the for the product ID
        idorder = input("inform the product ID: ").strip()



        # Check if the ID contains only numbers
        if not idorder.isdigit():

            print("Insert only positive inteer numbers")

            continue

        
        

        idorder = int(idorder)



        # Search the product by ID

        found_product = None

        for product in products:



            if product["id"] == idorder:

                found_product = product

                break





        # If the product was not found, ask again
        if found_product == None:

            print("Product not found, try again...")

            continue

        # checks if there are items in stock
        elif found_product['stock'] == 0:
        
            print("We don't have this item in stock at the moment.")

            continue

        print(f"Product found, ({found_product['name']})")



        # Loop to validate the product quantity
        while True:



            # Ask the client for the product quantity
            stockorder = input("Inform the quantity of product: ").strip()



            # Check if the quantity contains only numbers
            if not stockorder.isdigit():

                print("Insert only positive inteer numbers")

                continue



            stockorder = int(stockorder)

        

            # Check if there is enough stock
            if stockorder > found_product['stock']:

                print(f"Sorry, but we have only {found_product['stock']} unitys in stock. Please try again")

                continue



            # The quantity cannot be zero
            elif stockorder == 0:

                print("Insert a quanty greater than zero...")

                continue


            else:

                print("Sucess!")

                print(f"{stockorder} unitys of {found_product['name']} went into your cart")

                break


        # Check if the product is already in the order
        for productclient in orderclient:

            if productclient["id"] == idorder:

                # If the product already exists, update only the quantity
                productclient["quantity"] = stockorder

                print("Since this product has already been registered, only the quantity will be updated.")

                break


        # If the product is not in the order, add it
        else:

            order = {"id": idorder, "name": found_product["name"],"price": found_product["price"], "quantity": stockorder }

            orderclient.append(order)


        # Ask if the client wants to add another product
        again = input("You want to continue? Yes/No: ").strip().lower()



        # Check if the answer is valid
        while again not in ("yes","y","no","n"):

            print("Insert 'Yes' to add a new product in your order or 'no' for exit") 

            again = input("Do you want to continue? Yes/No: ").strip().lower()

                

        # if client wants to continue, the system returns to the main loop to add another product
        if again in ("yes","y"):

            continue

        

        elif again in ("no","n"):

            print(f"Your order: {orderclient}")


            # Ask the client to confirm the order
            confirm = input("Do you confirm your order? Yes/No: ").strip().lower()


            # Keep asking until the client gives a valid answer
            while confirm not in ("yes","y","no","n"):

                print("Insert 'Yes' to confirm the order or 'no' for cancel the order")

                confirm = input("Do you confirm your order? Yes/No: ").strip().lower()


            # Confirm the order
            if confirm in ("yes","y"):

                    print("Order successfully generated!")

                    # Change the order status after confirmation
                    orderstatus = "Activated"


                    # Search the ordered products in the inventory
                    for product1 in products:

                        for product2 in orderclient:


                            # Compare the products by ID
                            if product2["id"] == product1["id"]:


                                # Calculate and update the new stock
                                newstock = product1["stock"] - product2["quantity"] 

                                product1["stock"] = newstock

                                break               
                    break     

            # Cancel the order
            elif confirm in ("no","n"):

                print("Order successfully cancelled!")

                break


    # Return the order and its status
    return orderclient,orderstatus



products = [
    {"id": 101, "name": "Keyboard", "price": 150.00, "stock": 5},
    {"id": 102, "name": "Mouse", "price": 80.00, "stock": 8},
    {"id": 103, "name": "Monitor", "price": 1200.00, "stock": 3},
    {"id": 104, "name": "Headset", "price": 250.00, "stock": 6}
]

showorders = []
returntomenu = "y"

while returntomenu == "y":

    print("1 - List products")
    print("2 - Create order")
    print("3 - Cancel order")
    print("4 - Show orders")
    print("5 - Sales report")
    print("0 - Exit")

    option = input("Choose a option: ").strip().lower()
    option = option.replace(" ","")

    if option in ("1","1-listproducts","listproducts"):
        for i in range(len(products)):
            print(products[i])


    elif option in ("2","2-createorder","createorder"):

        orderclient, orderstatus = create_order(products,showorders)

        #Save this specific order to a list with all orders
        showorders.append(orderclient)
        
    #elif option in ("3","3-cancelorder","cancelorder"):

    elif option in ("4","4-showorders","showorders"):
        if showorders == []:
            print("So far, no requests have been saved.")
        else:
            for id,orderclient in enumerate(showorders,99):
                id += 1
                print(f"id order: {id}", orderclient)
            

    elif option in ("0","0-exit","exit"):
        print("The system will be shut down. Thank you for using the system.")
        returntomenu = "n"
