'''OOPS
Object Oriented Programming concepts

Class -blueprint'''

class Shirt:
	def __init__(self,color,size,price):
		self.color=color
		self.size=size
		self.price=price



#Object

shirt1=Shirt("black","L",300)
shirt2=Shirt("orange","XL",450)

#Abstarction

class ShirtStore:
	def buy_shirt(self):
		self.__check_inventory()
		self.__process_payment()
		print("Shirt purchased")
	def __check_inventory(self):
		print("Checking inventory")
	def __process_payment(self):
		print("Processing payment")

store=ShirtStore()
store.buy_shirt()


#Encapsulation

class Shirt:
	def __init__(self,price):
		self.price=price
	def get_price(self):
		return self.__price
	def set_price(self,price):
		if price>0:
			self.__price=price
shirt=Shirt(900)
print(shirt.get_price())


#Inheritence

class Shirt:
	def wear(self):
		print("Wearing Shirt")
class FormalShirt(Shirt):
	def office(self):
		print("Suitable for ofc")
shirt=FormalShirt()
shirt.wear()
shirt.office()

#Polymorphism

class Shirt:
	def wear(self):
		print("Wearing nrml shirt")
class FormalShirt(Shirt):
	def wear(self):
		print("Wearing formal shirt")
class TSHirt(Shirt):
	def wear(self):
		print("Wearing tshirt")
shirt=[FormalShirt(),TSHirt()]
for shirt in shirts:
	shirt.wear()
