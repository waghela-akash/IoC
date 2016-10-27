class Product:
	__productList = []	
	def __init__(self):
		pass

	def add(self,productName,price):
		self.__productList.append({'name':productName,'price':price})

	def getList(self):
		return self.__productList;

class Operations:
	def __init__(self,product):
		self.__product = product


	def isProduct(self, productName):
		allproduct = self.__product.getList();
		for it in allproduct[:]:
			if it['name'] != productName:
				allproduct.remove(it)
		return allproduct;

def main():
	flip = Product()
	flip.add("TV",1050)
	flip.add("TV",1150)
	flip.add("Fridge",10050)
	flip.add("Fridge",50000)
	flip.add("Fridge",10000)

	op = Operations(flip);
	out = op.isProduct("TV")
	print(out)

if __name__ == "__main__": main() 
