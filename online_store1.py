class Person:
    id_counter=100
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password
        self.person_id=Person.id_generator()
        
    @classmethod
    def id_generator(self):
        id=self.id_counter
        self.id_counter+=1
        return id

    def __repr__(self) -> str:
         return f"email: {self.email} and person id :{self.person_id}"
class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def __repr__(self) -> str:
        return f"product_name: {self.name} and product_price: {self.price} and product quantity: {self.quantity}"
    
class Store:
    def __init__(self) -> None:
          self.total_product={}

    def add_product(self,seller_id,product):
        #print(seller_id)
        product_dics=vars(product)
        #print(product_dics)
        if seller_id not in self.total_product:
            self.total_product[seller_id]=[]

            seller_info ={}
            seller_info["total_sell_product"]=0
            seller_info["total_sell_amount"]=0
            seller_info["total_sell_quantity"]=0
            self.total_product[seller_id].append(seller_info)
        self.total_product[seller_id].append(product_dics)

class Owner(Person):
    def __init__(self, email, password) -> None:
        self.total_sell_products=0
        self.total_sell_amount=0
        self.total_profit_amount=0
        super().__init__(email, password)
    def shop_info(self,store):
        all_seller_id=store.total_product.keys()
        #print(all_seller_id)
        for seller_id in all_seller_id:
            #print(seller_id)
            sell_info=store.total_product[seller_id][0]
            #print(sell_info)
            self.total_sell_products +=sell_info['total_sell_product']
            self.total_sell_amount +=sell_info['total_sell_amount']
        sell_info={
            'total_sell_product':self.total_sell_products,
            'total_sell_amount':self.total_sell_amount,
            'total_profit_amount':self.total_profit_amount
        }
        return sell_info
class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
    
    def add_product(self,store,product_name,product_price,product_quantity):
        product=Product(product_name,product_price,product_quantity)
        store.add_product(self.person_id,product) #this  person_id work as seller_id in Store class -> add_product method
    def sell_info(self,store):
        #print(self.person_id)
        print(store.total_product[self.person_id][0])
    

class Customer(Person):
    def __init__(self, email, password) -> None:
        self.total_buy_amount=0
        self.total_buy_products=0
        super().__init__(email, password)
    
    def show_products(self,product):
        all_keys=product.total_product.keys()
        for seller_id in all_keys:
            print("seller_id ", seller_id)
            print("<-----********************----->")
            for index in range(1,len(product.total_product[seller_id])):
                #print(product.total_product[seller_id][index]) #avoid first index of total_product dictionary..ha ha ha.
                product_with_skip_index=product.total_product[seller_id][index]
                print("name: ",product_with_skip_index["name"], " price: ",product_with_skip_index["price"]," quantity: ",product_with_skip_index['quantity'])
    
    def buy_product(self,store,seller_id,product_name,quantity):
        #print(store.total_product)
        #print(store.total_product[seller_id])
        for index in range(1,len(store.total_product[seller_id])):
            product=store.total_product[seller_id][index]
            if product['name']==product_name:
                #print(product)
                product['quantity']-=quantity
                self.total_buy_products +=quantity
                self.total_buy_amount +=product['price'] * quantity

                seller=store.total_product[seller_id][0]
                seller['total_sell_product']+=quantity
                seller['total_sell_amount']+=product['price']* quantity

seller1=Seller('hafize@sharkar.com','djfakjf4325')
seller2=Seller('shohag@bgfg09o0.com','090et9e87')
seller3=Seller('hangamara@gmail.com','kare9t9')

print(seller1)
print(seller2)
print(seller3) 
store=Store()
seller1.add_product(store,'laptop',65000,9)
seller1.add_product(store,'iphone',120000,3)

seller2.add_product(store,'pant',1200,10)
seller2.add_product(store,'lungi',600,10)

seller3.add_product(store,'purfume',129,10)
seller3.add_product(store,'lipstick',20,10)


print(store.total_product) # show product dictionary Store class

customr1=Customer('customer1@gamil.com','hakadrie535tr3')

customr1.show_products(store)

customr1.buy_product(store,100,'laptop',3)

print("****----****----****")


customr1.show_products(store)
print(store.total_product) # show product dictionary Store class

#check customer1 total_buy_product and total_buy_amount
print("total buy product ",customr1.total_buy_products,  "total_buy_amount: ",customr1.total_buy_amount)
 

customr1=Customer('customer1@gamil.com','hakadrie535tr3')
customr1.buy_product(store,100,'laptop',3)

seller1.sell_info(store)


owner=Owner('hafiz@gamil.com','ejtwqiert123424dkf')
print(owner.shop_info(store))





