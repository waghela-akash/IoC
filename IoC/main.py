import products as products
import operations as operations

import dependency_injector.containers as containers
import dependency_injector.providers as providers

class Products(containers.DeclarativeContainer):
	product = providers.Factory(products.Product)

class Operations(containers.DeclarativeContainer):
	operation = providers.Factory(operations.Operations, product=Products.product)

def main():
	flip = Products.product()
	flip.add("TV",1050)
	flip.add("TV",1150)
	flip.add("Fridge",10050)
	flip.add("Fridge",50000)
	flip.add("Fridge",10000)

	op = Operations.operation();
	out = op.isProduct("Fridg")
	print(out)

if __name__ == "__main__": main() 