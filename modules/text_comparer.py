import requests
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
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
        with ThreadPoolExecutor(multiprocessing.cpu_count()) as p:
            for i in range(0, len(self.url_list)):
                print("... downloading and writing file: " + str(i+1))
                self.download(self.url_list[i], 'book' + str(i+1) + ".txt")
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n != (len(self.url_list)):
            # Using split('/') and last element "[-1]" to get filename 
            result = self.url_list[self.n].split('/')[-1]
            self.n += 1
            return result
        else:
            raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        pass

    def hardest_read(self):
        pass
