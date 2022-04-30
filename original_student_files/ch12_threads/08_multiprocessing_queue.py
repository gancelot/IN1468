from multiprocessing import Process, freeze_support, Queue
from queue import Empty

from bs4 import BeautifulSoup
import requests

num_processes = 20
tasks = ['http://python-requests.org', 'https://pandas.pydata.org/', 'https://pypi.python.org',
         'https://flask.palletsprojects.com/en/1.1.x/', 'http://www.python.org', 'http://love-python.blogspot.com/',
         'http://planetpython.org', 'https://www.python.org/doc/humor/', 'https://rszalski.github.io/magicmethods/',
         'https://doughellmann.com/blog/', 'https://pymotw.com/3/', 'http://python-history.blogspot.com/',
         'https://nothingbutsnark.silvrback.com/', 'https://www.pydanny.com/','https://pythontips.com/',
         'http://www.blog.pythonlibrary.org/']


def get_data(url):
    """
        This is the work each process will perform (retrieve a page, extract the <title>).
    """
    try:
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'html.parser')
        result = soup.title.text
    except (TypeError, requests.exceptions.ConnectionError) as err:
        result = err.args[0]

    return result


def create_tasks(req_queue, tasks, num_processes):
    """
         The request_queue is populated with all of the URLs followed by sentinel values: "DONE" to signal when
         work is finished.
    """
    for url in tasks:
        req_queue.put(url)
    for i in range(num_processes):
        req_queue.put('DONE')


def work(req_queue, results_queue):
    """
        This is the target function for each thread.  It repeatedly grabs from the request_queue until it grabs the
        value "DONE" and then it terminates the work loop.
    """
    while True:
        try:
            val = req_queue.get(timeout=10)
            print(f'Grabbing from queue: {val}')
            if val == 'DONE':
                break
            results_queue.put(get_data(val))
        except TimeoutError:
            break


def print_results(results_queue):
    """
        Prints the results_queue.
    """
    while True:
        try:
            results = results_queue.get(block=False)
            print(f'Result: {results}')
        except Empty:
            break


def main():
    processes = []
    req_queue = Queue()
    results_queue = Queue()
    for i in range(num_processes):
        p = Process(target=work, args=(req_queue, results_queue))
        p.start()
        processes.append(p)

    create_tasks(req_queue, tasks, num_processes)

    for p in processes:
        p.join()

    print_results(results_queue)


if __name__ == '__main__':
    freeze_support()
    main()
