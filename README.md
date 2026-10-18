This project examines how unsafe string handling can corrupt stack memory in deliberately vulnerable C programs. The two parts demonstrate how an overflow can affect either an authentication variable or a saved return address.

Part 1: Authentication-Variable Overwrite

The first supplied program stores a salt and a password in a fixed-size buffer. Its password-length check does not account correctly for the space already occupied by the salt.

The solution constructs an input that extends beyond the buffer and changes a nearby authentication variable. This demonstrates that memory corruption can alter a program’s decision without changing its normal control flow.

Part 2: Saved Return-Address Overwrite

The second supplied program appends a password to a salted buffer without checking that the combined string fits.

The exercise follows a debugging and analysis workflow:

Provide a patterned input that causes the program to crash.

Inspect the resulting core dump in GDB.

Locate the input on the stack and identify which bytes overwrite the saved return address.

Determine the buffer address and the offset to that return address.

Construct a payload containing assembly code, padding, and a replacement address.

The assembly demonstrates execution of a shell within the original course lab environment. The address is encoded in little-endian order to match the target architecture.

Files

q1/q1.py: Authentication-variable overwrite demonstration.

q2.py: Patterned crash input for debugging.

q3.py: Payload construction for the second lab.

q2/shellcode.asm: x86 assembly used by the payload.

Environment and Limitations

The solutions depend on the original Linux lab environment and supplied vulnerable programs.

The second solution uses a fixed stack address and offset measured in that environment. Its behavior depends on the executable, architecture, memory layout, and lab configuration.

Original vulnerable programs and core dumps are not included in this code only upload.
