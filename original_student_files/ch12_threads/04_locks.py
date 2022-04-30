"""

    04_locks.py

    This example should be run two ways: 1) with the acquire()/release() commented out,  2) with them uncommented

    When the lock not used, each thread comes through the function, sets the internal_message which then sets
    the global message, therefore the last thread to pass through the line message = internal_message.

    When the lock is used, each thread must wait at the acquire().  One thread at a time is allowed passed acquire()
    and it gets the global message, assigns it to internal_message, appends its own message to internal_message,
    then sets the global one to the internal_message variable.  No other threads will interfere now.  After the
    release(), the next thread is allowed to repeat this process.

"""
from threading import Thread, Lock
from time import sleep

message = ''
lock = Lock()


def set_message(msg):
    global message

    # lock.acquire()

    internal_message = message                          # get the global message, assign it to the local message
    internal_message += msg                             # internal message will be 'First thread', 'Second thread', 'Third thread'
    sleep(0.3)
    message = internal_message                          # last one here gets to set the global value without a lock
                                                        # with a lock, only one thread at a time will set the global so
                                                        # the next thread will see the changed value by then
    print(f'Message: {internal_message}\n')

    # lock.release()


t1 = Thread(target=set_message, args=('First thread ',))
t2 = Thread(target=set_message, args=('Second thread ',))
t3 = Thread(target=set_message, args=('Third thread ',))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f'End Message: {message}')                # without a lock message will be whatever thread came last
