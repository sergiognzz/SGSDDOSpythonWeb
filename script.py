import socket
from urllib.parse import urlparse

url = "https://wiki-race.com/"

dominio = urlparse(url).hostname
ip = socket.gethostbyname(dominio)

print(ip)