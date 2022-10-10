import argparse
import textwrap

def parseArgs():
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
          ikitten.py -t 192.168.1.108 -p 5555 -l -c # command shell
          ikitten.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # upload to file
          ikitten.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
          echo 'ABCDEFGHI' | ./ikitten.py -t 192.168.1.108 -p 135 # echo local text to server port 135
          ikitten.py -t 192.168.1.108 -p 5555 # connect to server
          ikitten.py -t 192.168.1.108 -l -p 5555 # Listen for a reverse shell
          '''))
    parser.add_argument('-c', '--command', action='store_true', help='initialize command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    parser.add_argument('-s', '--peass', action='store_true', help="Upload and execute linPeass on the remote machine.")

    return parser.parse_args()

def printKitten():
    print(textwrap.dedent('''
       |\---/|
       | ,_, |
        \_`_/-..----.
     ___/ `   ' ,""+ \  IKitten
    (__...'   __\    |`.___.';
      (_,...'(_,.`__)/'.....+
    '''))
