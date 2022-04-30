from queue import Queue
from threading import Thread

from bs4 import BeautifulSoup
import requests

num_worker_threads = 20
tasks = ['http://python-requests.org', 'https://www.google.com', 'https://pypi.python.org',
         'https://www.cisco.com', 'http://www.python.org', 'http://love-python.blogspot.com/',
         'http://planetpython.org', 'https://www.python.org/doc/humor/', 'http://lucumr.pocoo.org/',
         'https://doughellmann.com/blog/', 'https://pymotw.com/3/', 'http://python-history.blogspot.com/',
         'https://nothingbutsnark.svbtle.com/','https://www.pydanny.com/','https://pythontips.com/',
         'http://www.blog.pythonlibrary.org/']


def get_data(url):
    try:
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'html.parser')
        result = soup.title.text
    except (TypeError, requests.exceptions.ConnectionError) as err:
        result = err.args[0]

    return result


req_queue = Queue()
results_queue = Queue()
for url in tasks:
    req_queue.put(url)


class WorkerThread(Thread):
    def run(self):
        while not req_queue.empty():
            url = req_queue.get()
            results_queue.put(get_data(url))
            req_queue.task_done()


for i in range(num_worker_threads):
    t = WorkerThread()
    t.start()


req_queue.join()       # don't end main thread until all tasks are finished

while not results_queue.empty():
    print(results_queue.get())
    results_queue.task_done()
