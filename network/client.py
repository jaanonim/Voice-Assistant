import json
import socket
import threading
import time

from utilities.command_processor import CommandProcessor
from utilities.settings import Settings


class Client:
    def __init__(self):
        self.size = 2048
        self.name = Settings.getInstance().get("name")
        self.server_port = Settings.getInstance().get("serverPort")
        self.server_addres = Settings.getInstance().get("serverAdres")

        print("[CLIENT] Starting...")
        thread = threading.Thread(name="client", target=self.connect)
        thread.start()

    def connect(self):
        while True:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                self.client.connect((self.server_addres, self.server_port))
                while True:
                    try:
                        self.send(f"ADD:{self.name}")
                    except Exception as e:
                        print(f"[CLIENT] {e}")
                        continue
                    msg = self.client.recv(self.size).decode()
                    code, info = msg.split(":", 1)
                    print(f"[CLIENT] {code} : {info}")
                    if code == "OK":
                        self.listen()
                    else:
                        time.sleep(5)

            except Exception as e:
                print(f"[CLIENT] {e}")
                print("[CLIENT] Cannot connect to server.")
                time.sleep(5)

    def listen(self):
        while True:
            msg = self.client.recv(self.size).decode()
            if not msg:
                continue
            code, info = msg.split(":", 1)
            print(f"[CLIENT] {code} : {info}")
            if code == "PING":
                self.send("OK:OK")
                continue
            if code == "COM":
                data = json.loads(info)
            comm_name = data.get("command")
            not_found = True
            for item in CommandProcessor.getInstance().commands:
                com, _ = item
                if com.__module__ == comm_name:
                    c = com()
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
