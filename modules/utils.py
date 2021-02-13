import sys
from os import listdir
from os.path import isfile, join
import os
sys.path.append(os.path.abspath('../'))
import pathlib

# Run in cli with: "python utils.py data_folder"
def get_file_names(folderpath,out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    content = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    content_string = ""
    for index in content:
        content_string += index + "\n"
    with open(out, 'w') as to_file_object:
            to_file_object.write(content_string)


def get_all_file_names(folderpath,out='output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    list_of_file = os.listdir(folderpath)
    all_files = list()
    for entry in list_of_file:
        full_path = os.path.join(folderpath, entry)

        if os.path.isdir(full_path):
            all_files = all_files + get_all_file_names(full_path)
        else:
            all_files.append(full_path)
                
    return all_files 

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""


if __name__ == '__main__':
    print_line_one(*sys.argv[1:])