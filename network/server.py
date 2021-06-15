import time
import asyncio
import socketio
import eventlet

# from utilities.settings import Settings


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

        self.clients = []
        self.socket = socketio.Server(async_mode="eventlet")
        self.name = "pc"  # Settings.getInstance().get("name")
        self.server_port = 5050  # Settings.getInstance().get("serverPort")
        self.server_addres = "192.168.0.27"  # Settings.getInstance().get("serverAdres")

    def run(self):
        print("[SERVER] Starting...")
        self.socket.register_namespace(ServerNamespace("/"))
        self.app = socketio.WSGIApp(self.socket)
        eventlet.wsgi.server(eventlet.listen(("", self.server_port)), self.app)


class ServerNamespace(socketio.Namespace):
    def on_connect(self, sid, environ, auth):
        if not auth in Server.getInstance().clients:
            print("[CLIENT] Connected!")
            Server.getInstance().clients.clients.append(auth)
        raise ConnectionRefusedError("authentication failed")

    def on_disconnect(self, sid):
        print("[CLIENT] Disconnected!.")

    async def on_command(self, sid, data):
        await self.emit("ok", data)


Server.getInstance().run()

"""
import json
import socket
import sys
import threading
import time

import schedule
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
        self.size = 1024
        self.port = Settings.getInstance().get("serverPort")
        self.addres = Settings.getInstance().get("serverAdres")
        self.connectino_msg = "HI MY NAME IS"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.addres, self.port))

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
                        conn.send(
                            str.encode("ERR:Name is taken! Pleace selcet other name.")
                        )
                        left -= 1
                    else:
                        print(f"[SERVER] {addr} registered with name: {name}.")
                        conn.send(str.encode("OK:Connected sucessfuly"))
                        self.clients[name] = conn
                        sys.exit()

        print(f"[SERVER] {addr} timeout.")
        conn.close()
        sys.exit()

    def keep_connection(self):
        schedule.every(5).minutes.do(self.test_connection)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def test_connection(self):
        print("ok")

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
                c.send(str.encode("COM:" + json.dump({"command": comm, "args": args})))
                msg = c.recv(self.size).decode()
                if msg:
                    code, info = msg.split(":")
                    if code == "OK":
                        data = json.loads(info)
                        return data["continue"], data["response"], None
                    else:
                        return False, msg, None
                raise
            except:
                self.clients.pop(name)
                return False, "Cannot send command to client.", None
        else:
            return False, "Wrong client name or clinet did not connect.", None
"""
