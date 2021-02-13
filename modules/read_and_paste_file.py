import csv
import sys

def print_file_content(path, file):
    path_content = []
    with open(path) as f:
        reader = csv.reader(f)
        for line in reader:
            path_content.append(line)
            
    content = ""
    for element in path_content:
        for line in element:
            content += line + " "
        content += "\n"
        
    with open(file, 'w') as to_file_object:
        to_file_object.write(content)

if __name__ == '__main__':
    print_file_content(*sys.argv[1:])
        
# Run like this in cli: python read_and_paste_file.py data_folder/addresses.csv data_folder/write_to_file.txt