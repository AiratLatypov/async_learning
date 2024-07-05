import asyncio
from asyncio import AbstractEventLoop
from threading import Thread
from chapter_07.event_loops_in_threads.tk_inter_gui_7_14 import LoadTester


class ThreadedEventLoop(Thread):  # A
    def __init__(self, loop_: AbstractEventLoop):
        super().__init__()
        self._loop = loop_
        self.daemon = True

    def run(self):
        self._loop.run_forever()


loop = asyncio.new_event_loop()

asyncio_thread = ThreadedEventLoop(loop)
asyncio_thread.start()  # B

app = LoadTester(loop)  # C
app.mainloop()
