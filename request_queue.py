import threading
import socketserver


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        self.server.queue.add(data)
        self.server.queue.set_client_adress(self.client_address)


class Queue:
    __client_addr = ("", 0)

    def __init__(self, ip, port):
        print("Init server:", ip, ":", port)
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server.queue = self
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.messages = []

    def start_server(self):
        self.server_thread.start()
        print("Running server thread")

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

    def add(self, message):
        self.messages.append(message)

    def set_client_adress(self, addr):
        self.__client_addr = tuple(addr)

    def get_client_adress(self):
        return self.__client_addr

    def view(self):
        return self.messages

    def get(self):
        return self.messages.pop()

    def exists(self):
        return len(self.messages)