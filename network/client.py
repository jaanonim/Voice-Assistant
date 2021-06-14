import json
import socket
import threading
import time

from utilities.settings import Settings
from utilities.command_processor import CommandProcessor


class Client:
    def __init__(self):
        self.size = 1024
        self.name = Settings.getInstance().get("name")
        self.server_port = Settings.getInstance().get("serverPort")
        self.server_addres = Settings.getInstance().get("serverAdres")
        self.connectino_msg = "HI MY NAME IS"

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
                    except Exception as e:
                        print(e)
                        continue
                    msg = self.client.recv(self.size).decode()
                    code, info = msg.split(":", 1)
                    print("[CLIENT] " + info)
                    if code == "OK":
                        self.listen()

            except Exception as e:
                print(e)
                print("[CLIENT] Cannot connect to server.")
                time.sleep(5)

    def listen(self):
        while True:
            msg = self.client.recv(self.size).decode()
            code, comm = msg.split(":", 1)
            if code == "COM":
                data = json.loads(comm)
            print(data)
            comm_name = data.get("command")
            not_found = True
            for item in CommandProcessor.getInstance().commands:
                if comm.__name__ == comm_name:
                    c = item()
                    c.values = data.get("args")
                    v, res, _ = c._execute()
                    self.send("OK:" + json.dumps({"continue": v, "response": res}))
                    not_found = False
                    break
            if not_found:
                self.send("ERR:Command not found!")

    def send(self, msg):
        message = msg.encode()
        self.client.send(message)
