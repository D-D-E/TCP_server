import json
import os
import files
from server import Server

CLIENT_PORT = 8687


class Socket(Server):

    def handle(self, message):
        try:
            data = json.loads(message)
            print(self.get_client_address(), ":", data)
            if data["command"] == "sayHello":
                self.send(self.get_client_address()[0], CLIENT_PORT, "hello")

            elif data["command"] == "getFileList":
                self.send(self.get_client_address()[0], CLIENT_PORT, json.dumps({"fileNames": folder.get_files_list()}))

            elif data["command"] == "getFile":
                if data["fileName"] in folder.get_files_list():
                    self.send(self.get_client_address()[0], CLIENT_PORT, folder.get_file(data["fileName"]))
                else:
                    self.send(self.get_client_address()[0], CLIENT_PORT, "file doesnt exist")

            elif data["command"] == "createFile":
                if data["fileName"]:
                    if "fileExtension" in data:
                        folder.create_file(data["fileName"], data["fileExtension"])
                    else:  # doesnt know why i separated name and extension
                        folder.create_file(data["fileName"], "")
            elif data["command"] == "updateFile":
                if data["fileName"] in folder.get_files_list():
                    folder.update_file(data["fileName"], data["fileData"])

            elif data["command"] == "appendFile":
                if data["fileName"] in folder.get_files_list():
                    folder.append_file(data["fileName"], data["fileData"])

            elif data["command"] == "deleteFile":
                if data["fileName"]:
                    folder.delete_file(data["fileName"])

            else:
                self.send(self.get_client_address()[0], CLIENT_PORT, "Error: not known command")
        except Exception as e:
            print("Error: {}".format(e))
            self.send(self.get_client_address()[0], CLIENT_PORT, "Error: {}".format(e))


if __name__ == "__main__":
    dir_name = os.path.dirname(os.path.abspath(__file__))
    filename = dir_name + "/folder_for_test"
    folder = files.Files(filename)

    app = Socket("192.168.1.144", 8686)
    app.start_server()
    app.loop()
    app.stop_server()
