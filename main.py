from network.client import Client
from network.server import Server
from utilities.command_processor import CommandProcessor
from utilities.io import IO
from utilities.settings import Settings


def main():
    Settings.getInstance()
    CommandProcessor.getInstance()
    if Settings.getInstance().get("isClient"):
        Client()
    else:
        Server.getInstance()
        IO().run()


if __name__ == "__main__":

    Client().run()
    # main()
