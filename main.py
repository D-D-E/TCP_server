import json
import os
import files
from server import Server


class Socket(Server):

    def handle(self, message):
        try:
            data = json.loads(message)
            print(self.get_client_address(), ":", data)
            if data["command"] == "sayHello":
                self.send(self.get_client_address()[0], 62848, "hello")
            elif data["command"] == "getFileList":
                self.send(self.get_client_address()[0], 62848, json.dumps({"file": folder.get_files_list()}))
            elif data["command"] == "getFile":
                if data["file"] in folder.get_files_list():
                    self.send(self.get_client_address()[0], 62848, folder.get_file(data["file"]))
                else:
                    self.send(self.get_client_address()[0], 62848, "file doesnt exist")
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == "__main__":
    dir_name = os.path.dirname(__file__)
    #there is path.join but itchanges / on \
    filename = dir_name + "/folder_for_test"
    folder = files.Files(filename)

    app = Socket("localhost", 8686)
    app.start_server()
    app.loop()
    app.stop_server()