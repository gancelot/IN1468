"""

    05_with.py

    Using RLocks and with
"""
from threading import Thread, RLock
from time import sleep

message = ''
lock = RLock()


def set_message(msg):
    global message

    with lock:
        internal_message = message
        internal_message += msg
        sleep(0.3)
        message = internal_message
        print(f'Message: {internal_message}\n')


t1 = Thread(target=set_message, args=('First thread ',))
t2 = Thread(target=set_message, args=('Second thread ',))
t3 = Thread(target=set_message, args=('Third thread ',))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f'End Message: {message}')
