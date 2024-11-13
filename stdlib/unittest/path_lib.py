import os

def replace_filename(file_path, file_name):
    directory_name = os.path.dirname(os.path.realpath(file_path))
    file_name = os.path.join(directory_name, file_name)
    return file_name

