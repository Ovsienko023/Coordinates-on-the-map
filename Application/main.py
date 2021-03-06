import json
from scripts.server.server import app
import sys
import os


def main():
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(*conf_server())


def conf_server():
    """Returns tuple(host, server) 
    from the file: config.txt.

    """
    path = os.getcwd() + "/Application/config.json"
    with open(path) as config:
        json_str = config.read()
        json_str = json.loads(json_str)

    host = json_str['server']['host']
    port = json_str['server']['port']
    return host, port


if __name__ == "__main__":
    main()
