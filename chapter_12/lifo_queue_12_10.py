import asyncio
from asyncio import Queue, LifoQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class WorkItem:
    priority: int
    order: int
    data: str = field(compare=False)


async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f"Processing work item {work_item}")
        queue.task_done()


async def main():
    """Элементы будут обрабатываться в порядке противоположном тому, в каком добавлялись."""
    lifo_queue = LifoQueue()

    work_items = [
        WorkItem(3, 1, "Lowest priority first"),
        WorkItem(3, 2, "Lowest priority second"),
        WorkItem(3, 3, "Lowest priority third"),
        WorkItem(2, 4, "Medium priority"),
        WorkItem(1, 5, "High priority"),
    ]

    worker_task = asyncio.create_task(worker(lifo_queue))

    for work in work_items:
        lifo_queue.put_nowait(work)

    await asyncio.gather(lifo_queue.join(), worker_task)



asyncio.run(main())

# Processing work item WorkItem(priority=1, order=5, data='High priority')
# Processing work item WorkItem(priority=2, order=4, data='Medium priority')
# Processing work item WorkItem(priority=3, order=3, data='Lowest priority third')
# Processing work item WorkItem(priority=3, order=2, data='Lowest priority second')
# Processing work item WorkItem(priority=3, order=1, data='Lowest priority first')
