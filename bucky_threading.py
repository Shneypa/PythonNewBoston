import threading

class BuckyMessenger(threading.Thread):

    def run(self):
        for _ in range(100):
            print(threading.current_thread().getName())

thread1 = BuckyMessenger(name = "Message sender active")
thread2 = BuckyMessenger(name = "Message receiver active")

thread1.start()
thread2.start()