import requests
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from tqdm import tqdm

class NotFoundException(Exception):
    pass


class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list

    def download(self, url, filename):
        response = requests.get(url)
        filename_full = 'data/' + filename

        if response.ok:
            with open(filename_full, 'wb') as file_object:
                file_object.write(response.content)
        elif response.status_code == 404:
            raise NotFoundException("No book was found using the given link!")

    def multi_download(self):
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as p:
            for i in range(0, len(self.url_list)):
                print("... downloading and writing file: " + str(i+1))
                self.download(self.url_list[i], 'book' + str(i+1) + ".txt")
    
    def __iter__(self):
        pass

    def __next__(self):
        pass

    def urllist_generator(self):
        pass

    def avg_vowels(self, text):
        pass

    def hardest_read(self):
        pass
