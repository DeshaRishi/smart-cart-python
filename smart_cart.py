class Product:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

class Store():
    def __init__(self):
        self.products = [
            Product(1,"iphone",1200000),
            Product(2,"samsung",800000),
            Product(3,'laptop',60000),
            Product(4,'samrtwatch',3000)
        ]
        self.cart=[]

    def ViewProducts(self):
        for product in self.products:
            print(f"{product.id}. {product.name} - {product.price}")

    def add_Products(self):
        product_id=int(input("Enter a product id: "))
        for product in self.products:
            if(product_id == product.id):
                   self.cart.append(product)
                   print("Item added to cart successfully")
                   return
        print("Item not found")

    def view_cart(self):
        if(len(self.cart)==0):
            print("Cart is empty")
            return
        total = 0
        for product in self.cart:
            total+=product.price

            print(f"{product.id}. {product.name} - {product.price}")
        print("Total cost: ", total)

    def remove_product(self):
        product_id = int(input("Enter a Product id to remove :"))
        for product in self.cart:
            if(product_id == product.id):
                self.cart.remove(product)
                print("Product removed from the cart successfully")
                return
        print("Item not found")

    def checkout(self):
        print("Order Placed Successfully")
        self.cart.clear()

    def run(self):
        while True:
            print("1. view products")
            print("2. add product")
            print("3. view cart")
            print("4. remove product")
            print("5. checkout ")
            print("6. exit")
            option=int(input("Choose a number "))
            if (option==1):
                self.ViewProducts()
            elif(option==2):
                self.add_Products()
            elif(option==3):
                self.view_cart()
            elif(option==4):
                self.remove_product()
            elif(option==5):
                self.view_cart()
            elif(option==6):
                print("exit")
                break
            else:
                print("Invalid option")

        

s1=Store()
s1.run()            





              





# s1=Store()
# s1.ViewProducts()
# s1.view_cart()
# s1.add_Products()
# s1.view_cart()
# s1.add_Products()
# s1.remove_product()
# s1.view_cart()
# s1.checkout()
# s1.run()


# p1 = Product(1,"iphone",120000)
# print(p1.name)
