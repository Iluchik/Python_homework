from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Purchase(BaseModel):
	prod_positions: dict[str, int]

class Product(BaseModel):
	name: str
	quantity: int
	cost: int

	def inc_quantity(self, num: int):
		self.quantity += num
		return
	
	def dec_quantity(self, num: int):
		if num > self.quantity:
			raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Not enough products in warehouse")
		self.quantity -= num
		return

	def cost_calculation(self):
		return self.quantity * self.cost

class Warehouse(BaseModel):
	prod_list: list[Product]
	sale_history: list[dict] | None

	def add_prod(self, product: Product):
		self.prod_list.append(product)
		return
	
	def pop_prod(self, product: Product | int):
		find_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
		if type(product) is int:
			try:
				poped_prod = self.prod_list.pop(product)
				if poped_prod is None:
					raise find_exception
			except IndexError:
				raise find_exception
		else:
			try:
				self.prod_list.remove(product)
				poped_prod = product
			except ValueError:
				raise find_exception
		return poped_prod
	
	def cost_calculation(self):
		sum_cost = 0
		for prod in self.prod_list:
			sum_cost += prod.cost_calculation()
		return sum_cost

class Seller(BaseModel):
	name: str
	revenue: dict[str, int] | None = {"Общая стоимость": 0}

	def sale(self, cheque: Purchase, store: Warehouse):
		sold_list = cheque.prod_positions.keys()
		for_sale = list(filter(lambda prod: prod.name in sold_list, store.prod_list))
		for prod in for_sale:
			prod.dec_quantity(cheque.prod_positions[f"{prod.name}"])
			if prod.name not in self.revenue.keys():
				self.revenue[prod.name] = cheque.prod_positions[f"{prod.name}"]
			else:
				self.revenue[prod.name] += cheque.prod_positions[f"{prod.name}"]
			self.revenue["Общая стоимость"] += prod.cost * cheque.prod_positions[f"{prod.name}"]
		store.sale_history.append({"time": f"{datetime.now()}", "prod_positions": cheque.prod_positions})
		return cheque
	
	def sales_report(self):
		return self.revenue

store = Warehouse(prod_list=[
	Product(name="Диван", quantity=26, cost=48000),
	Product(name="Кресло", quantity=42, cost=12000),
	Product(name="Стол", quantity=32, cost=23000),
	Product(name="Стул", quantity=108, cost=8500),
	Product(name="Шкаф", quantity=28, cost=58000)
], sale_history=[])

ivan = Seller(name="Ivan")

@app.post("/warehouse", response_model=list[Product])
async def new_product(product: Product):
	for prod in store.prod_list:
		if prod.name == product.name:
			raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already exist")
	store.add_prod(product)
	return store.prod_list

@app.delete("/warehouse", response_model=list[Product])
async def del_product(product: Product | int):
	store.pop_prod(product)
	return store.prod_list

@app.get("/warehouse", response_model=list[dict])
async def get_history():
	return store.sale_history

@app.post("/seller", response_model=Purchase)
async def sell(cheque: Purchase):
	return ivan.sale(cheque, store)

@app.get("/seller", response_model=dict[str, int])
async def get_revenue():
	return ivan.revenue

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)