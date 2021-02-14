import sys
from os import listdir
from os.path import isfile, join
import os
sys.path.append(os.path.abspath('../'))
import pathlib

# Run in cli with: "python utils.py data_folder"
def get_file_names(folderpath,out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    content = [file for file in listdir(folderpath) if isfile(join(folderpath, file))]
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

# I can't figure out how to take of list of strings in command line so this function only works for 1 string argument.
def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    #for file in file_names:
    with open(file_names, 'r') as file_object: 
        print(file_object.readline().strip())

# I can't figure out how to take of list of strings in command line so this function only works for 1 string argument.
def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    #for file in file_names:
    with open(file_names, 'r') as file_object: 
        content = file_object.readlines()
    
    for line in content:
        if '@' in line:
            print(line.strip())

# I can't figure out how to take of list of strings in command line so this function only works for 1 string argument.
def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    #for file in md_files:
    with open(md_files, 'r') as file_object: 
        content = file_object.readlines()
    
    with open(out, 'r+') as to_file_object:
        to_file_object.seek(0)
        to_file_object.truncate()
        for line in content:
            if '#' in line:
                to_file_object.write(line.strip() + "\n")

if __name__ == '__main__':
    # get_file_names in command line: "python utils.py data_folder" then see "output.txt" for result.
    #get_file_names(*sys.argv[1:])
    
    # get_all_file_names in command line: "python utils.py data_folder" then see command line for result.
    #print(get_all_file_names(*sys.argv[1:]))
    
    # print_line_one in command line: "python utils.py data_folder/a_file.txt" or "python utils.py data_folder/another_file.txt" then see command line for result.
    #print_line_one(*sys.argv[1:])
    
    # print_emails in command line: "python utils.py data_folder/a_file.txt" or "python utils.py data_folder/another_file.txt" then see command line for result.
    #print_emails(*sys.argv[1:])
    
    # write_headlines in command line: "python utils.py data_folder/md_test.md" then see "output.txt" for result.
    #write_headlines(*sys.argv[1:])