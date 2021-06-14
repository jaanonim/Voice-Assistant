from network.client import Client
from network.server import Server
from settings import Settings
from utilities.command_processor import CommandProcessor
from utilities.io import IO


def main():
    CommandProcessor.getInstance()
    if Settings.getInstance().get("isClient"):
        Client()
    else:
        Server.getInstance()
        IO().run()


if __name__ == "__main__":
    main()
