import sys
import os
from subprocess import Popen, PIPE

def main():
    args = sys.argv
    args[0] = os.path.join(os.getcwd(), "tool.py")
    args.insert(0, sys.executable)
    proc = Popen(args, stdout=PIPE, encoding="utf-8")
    out, err = proc.communicate()

    print(out)
    with open("out.txt", "w+") as f:
        print(out, file=f)

if __name__ == "__main__":
    main()
