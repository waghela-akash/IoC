class Operations:
	def __init__(self, product):
		self.__product = product # Injecting Dependency

	def isProduct(self, productName):
		allproduct = (self.__product).getList();
		for it in allproduct[:]:
			if it['name'] != productName:
				allproduct.remove(it)
		return allproduct;