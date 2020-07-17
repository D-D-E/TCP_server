import glob
import os
import binascii


class Files:
    __path = ""

    def __init__(self, path):
        self.__path = path

    def get_files_list(self):
        files = []
        os.chdir(self.__path)
        for file in glob.glob("*.*"):
            files.append(file)
        return files

    def get_file(self, file_name):
        file = self.__path + "/" + file_name
        print(file)
        with open(file, 'rb') as f:
            return f.read().hex()
        #return open(file, 'rb').read()
