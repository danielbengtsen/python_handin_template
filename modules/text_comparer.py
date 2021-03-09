import requests
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


class NotFoundException(Exception):
    pass


class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list

    def download(self, url, filename):
        response = requests.get(url)
        filename_full = 'data_folder/' + filename

        if response.ok:
            with open(filename_full, 'wb') as file_object:
                file_object.write(response.content)
        elif response.status_code == 404:
            raise NotFoundException("No book was found using the given link!")

    def multi_download(self):
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as p:
            for i in range(0, len(self.url_list)):
                self.download(self.url_list[i], 'book' + str(i+1) + ".txt")


url_list = ["https://www.gutenberg.org/files/11/11-0.txt", "https://www.gutenberg.org/files/74/74-0.txt", "https://www.gutenberg.org/files/730/730-0.txt", "https://www.gutenberg.org/ebooks/4363.txt.utf-8", "https://www.gutenberg.org/files/84/84-0.txt",
            "https://www.gutenberg.org/files/35/35-0.txt", "https://www.gutenberg.org/files/42108/42108-0.txt", "https://www.gutenberg.org/files/6130/6130-0.txt", "https://www.gutenberg.org/files/16/16-0.txt", "https://www.gutenberg.org/files/160/160-0.txt"]
tc = TextComparer(url_list)
#tc.download(url_list[0], 'book_1.txt')
# tc.multi_download()
