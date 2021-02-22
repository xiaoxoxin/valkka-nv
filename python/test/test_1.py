import time
from valkka.hw import ExampleThread

t = ExampleThread("test_thread")

t.startCall()

time.sleep(10)

t.stopCall()
