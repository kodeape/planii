from os import listdir

def read_file_lines(file):
    file = open(file, 'r')
    lines = file.readlines()
    file.close()
    return lines

def write_to_file(file, text):
    file = open(file, 'w')
    file.write(text)
    file.close()

def write_file_lines(file, lines):
    file = open(file, 'r')
    for line in lines:
        file.write(line)
    file.close()

def files_in_dir(dir):
    return listdir(dir)