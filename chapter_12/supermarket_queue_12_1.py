import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time

    def __repr__(self):
        return self.name


class Customer:
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():
        customer: Customer = queue.get_nowait()  # есть блокирующий метод get, который будет ждать пока не
        # появится покупатель. В этом случае условие while not будет не нужно.
        print(
            f"Cashier {cashier_number} "
            f"checking out customer "
            f"{customer.customer_id}"
        )
        for product in customer.products:
            print(
                f"Cashier {cashier_number} "
                f"checking out customer "
                f"{customer.customer_id}: {product.name}"
            )
            await asyncio.sleep(product.checkout_time)
        print(
            f"Cashier {cashier_number} "
            f"finished checking out customer "
            f"{customer.customer_id}"
        )
        queue.task_done()


async def main():
    customer_queue = Queue()

    all_products = [
        Product("beer", 2),
        Product("bananas", .5),
        Product("sausage", .2),
        Product("diapers", .2),
    ]

    for i in range(10):
        products = [
            all_products[
                randrange(len(all_products))
            ] for _ in range(randrange(10))
        ]
        customer_queue.put_nowait(Customer(i, products))

    cashiers = [
        asyncio.create_task(checkout_customer(customer_queue, i))
        for i in range(3)
    ]

    await asyncio.gather(customer_queue.join(), *cashiers)

asyncio.run(main())

# Cashier 0 checking out customer 0
# Cashier 0 checking out customer 0: diapers
# Cashier 1 checking out customer 1
# Cashier 1 finished checking out customer 1
# Cashier 1 checking out customer 2
# Cashier 1 checking out customer 2: beer
# Cashier 2 checking out customer 3
# Cashier 2 checking out customer 3: bananas
# Cashier 0 checking out customer 0: beer
# Cashier 2 finished checking out customer 3
# Cashier 2 checking out customer 4
# Cashier 2 checking out customer 4: bananas
# Cashier 2 checking out customer 4: bananas
# Cashier 2 finished checking out customer 4
# Cashier 2 checking out customer 5
# Cashier 2 checking out customer 5: bananas
# Cashier 1 checking out customer 2: sausage
# Cashier 2 checking out customer 5: beer
# Cashier 0 checking out customer 0: beer
# Cashier 1 checking out customer 2: diapers
# Cashier 1 checking out customer 2: diapers
# Cashier 1 checking out customer 2: beer
# Cashier 2 checking out customer 5: diapers
# Cashier 2 checking out customer 5: beer
# Cashier 0 checking out customer 0: bananas
# Cashier 1 checking out customer 2: sausage
# Cashier 0 finished checking out customer 0
# Cashier 0 checking out customer 6
# Cashier 0 checking out customer 6: beer
# Cashier 1 checking out customer 2: sausage
# Cashier 1 checking out customer 2: sausage
# Cashier 1 checking out customer 2: beer
# Cashier 2 checking out customer 5: sausage
# Cashier 2 checking out customer 5: diapers
# Cashier 2 finished checking out customer 5
# Cashier 2 checking out customer 7
# Cashier 2 checking out customer 7: bananas
# Cashier 0 checking out customer 6: beer
# Cashier 2 checking out customer 7: beer
# Cashier 1 finished checking out customer 2
# Cashier 1 checking out customer 8
# Cashier 1 finished checking out customer 8
# Cashier 1 checking out customer 9
# Cashier 1 checking out customer 9: sausage
# Cashier 1 checking out customer 9: sausage
# Cashier 1 checking out customer 9: diapers
# Cashier 1 checking out customer 9: bananas
# Cashier 1 checking out customer 9: sausage
# Cashier 1 checking out customer 9: bananas
# Cashier 0 checking out customer 6: sausage
# Cashier 0 finished checking out customer 6
# Cashier 1 checking out customer 9: bananas
# Cashier 2 checking out customer 7: beer
# Cashier 1 finished checking out customer 9
# Cashier 2 checking out customer 7: beer
# Cashier 2 finished checking out customer 7
