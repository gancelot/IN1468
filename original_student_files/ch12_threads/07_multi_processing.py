import multiprocessing
import os
import time


def square(val: int):
    time.sleep(2) # just to slow it down so it can be viewed easier
    print(f'\nSquare result: {val * val}, process id: {os.getpid()}')


def cube(val: int):
    time.sleep(2)
    print(f'\nCube result: {val ** 3}, , process id: {os.getpid()}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=square, args=(4,))
    p2 = multiprocessing.Process(target=cube, args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('Tasks done!')
