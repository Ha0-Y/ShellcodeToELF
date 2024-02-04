# ShellcodeToELF

Linux下使用 `nasm` 生成可执行文件，需要使用 `ld` 链接，最终生成文件比较大，如何生成很小的ELF文件呢？

**只关注 64 位下可执行文件。**

usage:
```bash
$ python main.py -i test.asm -o test.bin
```

test.asm format reference: test.asm
```asm
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
```

FIX BUG: 不能执行如下的汇编，必须是 `xor DWORD PTR [rsp], 0x1010101`
```asm
push 0x1016660
xor DWORD [rsp], 0x1010101
```

## 生成

只需要提供一个 `asm` 文件