import threading
import time
import random


class Philosopher(threading.Thread):

    def __init__(self, name, leftFork, rightFork):
        print("{} сів за стіл".format(name))
        threading.Thread.__init__(self, name=name)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print("{} почав думати".format(threading.current_thread().name))
        while True:
            time.sleep(random.randint(1, 5))
            print("\n{} закінчив думати".format(threading.current_thread().name))
            self.leftFork.acquire()
            time.sleep(random.randint(1, 5))
            try:
                print("{} отримав виделку зліва".format(threading.current_thread().name))

                self.rightFork.acquire()
                try:
                    print("{} володіє обома виделками, зараз їсть".format(threading.current_thread().name))
                finally:
                    self.rightFork.release()
                    print("{} віддав праву виделку".format(threading.current_thread().name))
            finally:
                self.leftFork.release()
                print("{} віддав ліву виделку".format(threading.current_thread().name))


fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

philosopher1 = Philosopher("Кант", fork1, fork2)
philosopher2 = Philosopher("Арістотель", fork2, fork3)
philosopher3 = Philosopher("Спіноза", fork3, fork4)
philosopher4 = Philosopher("Маркс", fork4, fork5)
philosopher5 = Philosopher("Рассел", fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()

# import threading
# import time
#
# balance = 100000
#
#
# def withdrawal():
#     global balance
#     time.sleep(1)
#     balance -= 10000
#     print("Balance = {}".format(balance))
#
#
# if __name__ == "__main__":
#     i = 0
#     while balance > 0:
#         # creating threads
#         t1 = threading.Thread(target=withdrawal)
#
#         # start threads
#         t1.start()
#         time.sleep(0.1)
#
#         t2 = threading.Thread(target=withdrawal)
#         t2.start()
#
#         # wait until threads finish their job
#
#         i += 1
#         t1.join()
#         t2.join()
#         print("Iteration {0}: x = {1}".format(i, balance))
