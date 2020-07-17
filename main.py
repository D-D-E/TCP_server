import json
from server import Server


class Socket(Server):

    def handle(self, message):
        try:
            data = json.loads(message)
            print(self.get_client_address(), ":", data)
            if data["command"] == "sayHello":
                self.send(self.get_client_address()[0], 62848, "hello")
            elif data["command"] == "getFileList":
                files = ["save1.any", "save2.any", "save3.any"]
                self.send(self.get_client_address()[0], 62848, json.dumps(files))
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == "__main__":

    app = Socket("localhost", 8686)
    app.start_server()
    app.loop()
    app.stop_server()