import urllib.request
import time
import threading


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
for url in urls:
    read_url(url)
print("Time = ", (time.time() - start))

def thread_job(url):
    with urllib.request.urlopen(url) as u:
        return u.read()

urls = [
        'https://www.yandex.ru', 'https://www.google.com',
        'https://habrahabr.ru', 'https://www.python.org',
        'https://isocpp.org',
    ]
start = time.time()
n = len(urls)
threads = [threading.Thread(target=thread_job(urls[i])) for i in range(n)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("ThreadingTime = ", (time.time() - start))