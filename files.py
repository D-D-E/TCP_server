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
        print("Read: ", file)
        with open(file, 'rb') as f:
            return f.read().hex()

    def create_file(self, file_name, file_ext):
        if not file_ext:
            file = self.__path + "/" + file_name
        else:
            file = self.__path + "/" + file_name + "." + file_ext
        print("Created: ", file)
        f = open(file, "w")
        f.close()

    def delete_file(self, file_name):
        file = self.__path + "/" + file_name
        print("Deleted: ", file)
        if os.path.exists(file):
            os.remove(file)

    def update_file(self, file_name, data):
        file = self.__path + "/" + file_name
        print("Updated: ", file)
        with open(file, "w") as f:
            f.write(data)
            f.close()

    def append_file(self, file_name, data):
        file = self.__path + "/" + file_name
        print("Updated with append: ", file)
        with open(file, "a+") as f:
            f.write(data)
            f.close()