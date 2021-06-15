import json
import socket
import sys
import threading
import time

from utilities.settings import Settings


class Server:
    __instance = None

    @staticmethod
    def getInstance():
        if Server.__instance == None:
            Server()
        return Server.__instance

    def __init__(self):

        if Server.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Server.__instance = self

        self.clients = {}
        self.size = 2048
        self.port = Settings.getInstance().get("serverPort")
        self.addres = Settings.getInstance().get("serverAdres")
        self.connectino_msg = "HI MY NAME IS"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind((self.addres, self.port))
        except Exception as e:
            print(f"[SERVER] {e}")
            exit()
        print("[SERVER] Starting...")
        thread = threading.Thread(name="server", target=self.run)
        thread.start()

    def handle_client(self, conn, addr):
        print(f"[SERVER] {addr} connected.")

        left = 3
        while left > 0:
            msg = conn.recv(self.size).decode()
            if msg:
                if f"{self.connectino_msg} " in msg:
                    _, name = msg.split(f"{self.connectino_msg} ")
                    if self.clients.get(name):
                        if self.ping(name):
                            conn.send(
                                str.encode(
                                    "ERR:Name is taken! Pleace selcet other name."
                                )
                            )
                            left -= 1
                            continue
                    print(f"[SERVER] {addr} registered with name: {name}.")
                    conn.send(str.encode("OK:Connected sucessfuly"))
                    self.clients[name] = conn
                    sys.exit()

        print(f"[SERVER] {addr} timeout.")
        conn.close()
        sys.exit()

    def ping(self, name):
        other = self.clients.get(name)
        try:
            other.send(str.encode(f"PING:{name}"))
            msg = other.recv(self.size).decode()
            if not "OK" in msg:
                raise
        except:
            print(f"[SERVER] {name} diconnected (not responding).")
            other.close()
            self.clients.pop(name)
            return False
        print(f"[SERVER] {name} is still alive.")
        return True

    def run(self):
        self.server.listen()
        print(f"[SERVER] Server is listening on {self.port}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def sendCommand(self, name, comm, args):
        c = self.clients.get(name)
        if c:
            try:
                c.send(str.encode("COM:" + json.dumps({"command": comm, "args": args})))
                msg = c.recv(self.size).decode()
                if msg:
                    code, info = msg.split(":", 1)
                    if code == "OK":
                        data = json.loads(info)
                        return data["continue"], data["response"], None
                    return False, msg, None
            except Exception as e:
                print(f"[SERVER] {e}")
                c.close()
                self.clients.pop(name)
                return False, "Cannot send command to client.", None
        else:
            return False, "Wrong client name or clinet did not connect.", None
