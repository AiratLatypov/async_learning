import asyncio
from asyncio import Queue
from random import randrange


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id, products):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while True:
        customer: Customer = await queue.get()
        print(
            f"Cashier {cashier_number} "
            f"checking out customer "
            f"{customer.customer_id}"
        )
        for product in customer.products:
            print(
                f"Cashier {cashier_number} "
                f"checking out customer "
                f"{customer.customer_id}'s {product.name}"
            )
            await asyncio.sleep(product.checkout_time)
        print(
            f"Cashier {cashier_number} "
            f"finished checking out customer "
            f"{customer.customer_id}"
        )
        queue.task_done()


def generate_customer(customer_id: int) -> Customer: #A
    all_products = [
        Product("beer", 2),
        Product("bananas", .5),
        Product("sausage", .2),
        Product("diapers", .2),
    ]
    products = [
        all_products[
            randrange(len(all_products))
        ] for _ in range(randrange(10))
    ]
    return Customer(customer_id, products)


async def customer_generator(queue: Queue):
    customer_count = 0

    while True:
        customers = [
            generate_customer(i)
            for i in range(customer_count, customer_count + randrange(5))
        ]
        for customer in customers:
            print("Waiting to put customer in line...")
            await queue.put(customer)  # блокирующий метод put
            print("Customer put in line!")
        customer_count = customer_count + len(customers)
        await asyncio.sleep(1)


async def main():
    customer_queue = Queue(5) # добавляем максимальный размер очереди

    customer_producer = asyncio.create_task(customer_generator(customer_queue))

    cashiers = [
        asyncio.create_task(checkout_customer(customer_queue, i))
        for i in range(3)
    ]
    await asyncio.gather(customer_producer, *cashiers)


asyncio.run(main())

# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Cashier 0 checking out customer 0
# Cashier 0 checking out customer 0's diapers
# Cashier 1 checking out customer 1
# Cashier 1 checking out customer 1's bananas
# Cashier 2 checking out customer 2
# Cashier 2 finished checking out customer 2
# Cashier 0 checking out customer 0's bananas
# Cashier 1 checking out customer 1's diapers
# Cashier 0 checking out customer 0's sausage
# Cashier 1 checking out customer 1's beer
# Cashier 0 checking out customer 0's beer
# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Cashier 2 checking out customer 3
# Cashier 2 checking out customer 3's beer
# Cashier 1 checking out customer 1's bananas
# Cashier 0 checking out customer 0's diapers
# Cashier 2 checking out customer 3's bananas
# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Cashier 0 finished checking out customer 0
# Cashier 0 checking out customer 4
# Cashier 0 checking out customer 4's diapers
# Cashier 1 checking out customer 1's bananas
# Cashier 0 checking out customer 4's diapers
# Cashier 2 checking out customer 3's bananas
# Cashier 0 checking out customer 4's beer
# Cashier 1 checking out customer 1's beer
# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Waiting to put customer in line...
# Cashier 2 checking out customer 3's sausage
# Cashier 2 checking out customer 3's diapers
# Cashier 2 finished checking out customer 3
# Cashier 2 checking out customer 5
# Cashier 2 checking out customer 5's diapers
# Customer put in line!
# Cashier 2 checking out customer 5's bananas
# Cashier 2 checking out customer 5's sausage
# Cashier 2 checking out customer 5's diapers
# Waiting to put customer in line...
# Cashier 0 checking out customer 4's diapers
# Cashier 2 checking out customer 5's diapers
# Cashier 1 finished checking out customer 1
# Cashier 1 checking out customer 6
# Cashier 1 checking out customer 6's sausage
# Cashier 0 checking out customer 4's beer
# Cashier 2 checking out customer 5's sausage
# Customer put in line!
# Waiting to put customer in line...
# Cashier 1 checking out customer 6's beer
# Cashier 2 finished checking out customer 5
# Cashier 2 checking out customer 7
# Cashier 2 checking out customer 7's diapers
# Customer put in line!
# Waiting to put customer in line...
# Cashier 2 checking out customer 7's beer
# Cashier 0 checking out customer 4's diapers
# Cashier 1 checking out customer 6's sausage
# Cashier 0 checking out customer 4's bananas
# Cashier 1 checking out customer 6's sausage
# Cashier 2 checking out customer 7's sausage
# Cashier 1 checking out customer 6's bananas
# Cashier 2 checking out customer 7's beer
# Cashier 0 checking out customer 4's diapers
# Cashier 0 finished checking out customer 4
# Cashier 0 checking out customer 8
# Cashier 0 finished checking out customer 8
# Cashier 0 checking out customer 9
# Cashier 0 checking out customer 9's bananas
# Customer put in line!
# Waiting to put customer in line...
# Customer put in line!
# Cashier 1 finished checking out customer 6
# Cashier 1 checking out customer 10
