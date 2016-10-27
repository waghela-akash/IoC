class Product:
	__productList = []	
	def __init__(self):
		pass

	def add(self,productName,price):
		self.__productList.append({'name':productName,'price':price})

	def getList(self):
		return self.__productList;