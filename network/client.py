import json
import socket
import threading
import time

from settings import Settings


class Client:
    def __init__(self, commands):
        self.size = 1024
        self.name = Settings.getInstance().get("name")
        self.server_port = Settings.getInstance().get("serverPort")
        self.server_addres = "192.168.0.27"
        self.connectino_msg = "HI MY NAME IS"
        self.commands = commands

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[CLIENT] Starting...")
        thread = threading.Thread(name="client", target=self.connect)
        thread.start()

    def connect(self):
        while True:
            try:
                self.client.connect((self.server_addres, self.server_port))
                while True:
                    try:
                        self.send(f"{self.connectino_msg} {self.name}")
                    except:
                        break
                    msg = self.client.recv(self.size).decode()
                    code, info = msg.split(":", 1)
                    print("[CLIENT] " + info)
                    if code == "OK":
                        return

            except Exception as e:
                print(e)
                print("[CLIENT] Cannot connect to server.")
                time.sleep(5)
        self.listen()

    def listen(self):
        while True:
            msg = self.client.recv(self.size).decode()
            code, comm = msg.split(":", 1)
            if code == "COM":
                data = json.loads(comm)
            print(data)
            com_name = data.get("command")
            not_found = True
            for com in self.commands:
                if comm.__name__ == com_name:
                    com()
                    com.values = data.get("args")
                    v, res, _ = com._execute()
                    self.send("OK:" + json.dumps({"continue": v, "response": res}))
                    not_found = False
                    break
            if not_found:
                self.send("ERR:Command not found!")

    def send(self, msg):
        message = msg.encode()
        client.send(message)
