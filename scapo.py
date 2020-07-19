import socket
import pyfiglet
import sys
from datetime import datetime

# colored text and background


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


design = pyfiglet.figlet_format("SCAPO")
print("\n")
print(design)

# getting host
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    prRed("Invalid number of arguments")
    prRed("Format python3 scapo.py <IP>")
    sys.exit()

# adding some stuff
print("*"*40)
print("Scanning target " + target)
print("Started at : " + str(datetime.now()))
print("*"*40)
print("\n")

# checking for open ports
for port in range(1, 65535):
    try:
        # forming a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket.setdefaulttimeout(1)

        # this will return whether port is open or not
        stat = s.connect_ex((target, port))

        if stat == 0:
            prGreen("Port open {}".format(port))

        # closing the socket
        s.close()

    except KeyboardInterrupt:
        prRed("\nExiting the program !!!!")
        sys.exit()

    except socket.gaierror:
        prRed("Hostname could not be resolved !!!!")
        sys.exit()

    except socket.error:
        prRed("\nServer not responding !!!!")
        sys.exit()

print("\n")
print("*"*40)
print("Ended at : " + str(datetime.now()))
print("*"*40)
print("\n")
