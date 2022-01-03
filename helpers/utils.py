import os

def _delete_file_(path):
    if os.path.isfile(path):
        os.remove(path)