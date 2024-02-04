import argparse
from ctypes import sizeof, string_at, addressof
from keystone import Ks
from keystone import KS_ARCH_X86, KS_MODE_64

from elfhdr import Elf64_Ehdr
from elfhdr import Elf64_Phdr


class ElfBuiler:
    def __init__(self):
        self.elf_header = None
        self.elf_pheader = None
        self.outf = "shellcode.bin"
        self.EI_CLASS = 0x2
        self.vaddr = 0x400000
        self.e_machine = 0x3E

    def build_elf_header(self):
        self.elf_header = Elf64_Ehdr()
        self.elf_header.e_ident = (
            0x7f,
            ord("E"),
            ord("L"),
            ord("F"),
            self.EI_CLASS,
            0x1,
            0x1
        )
        self.elf_header.e_type = 0x2
        self.elf_header.e_machine = self.e_machine
        self.elf_header.e_version = 0x1
        self.elf_header.e_entry = 0x0

        self.elf_header.e_phoff = sizeof(Elf64_Ehdr)
        self.elf_header.e_shoff = 0x0
        self.elf_header.e_flags = 0x0
        self.elf_header.e_ehsize = sizeof(Elf64_Ehdr)

        self.elf_header.e_phentsize = sizeof(Elf64_Phdr)
        self.elf_header.e_phnum = 0x1
        self.elf_header.e_shentsize = 0x0
        self.elf_header.e_shnum = 0x0
        self.elf_header.e_shstrndx = 0x0
        return self.elf_header

    def build_elf_pheader(self, va):
        self.elf_pheader = Elf64_Phdr()
        self.elf_pheader.p_type = 0x1
        self.elf_pheader.p_flags = 0x7
        self.elf_pheader.p_offset = 0x0
        self.elf_pheader.p_vaddr = va
        self.elf_pheader.p_paddr = va
        self.elf_pheader.p_filesz = 0
        self.elf_pheader.p_memsz = 0
        self.elf_pheader.p_align = 0x1000
        return self.elf_pheader

    def generate_elf(self, evilcode: bytes, outf: str):
        self.build_elf_header()
        self.build_elf_pheader(0x400000)

        self.elf_header.e_entry = self.elf_pheader.p_vaddr + sizeof(self.elf_header) + sizeof(self.elf_pheader)
        self.elf_pheader.p_filesz = sizeof(self.elf_header) + sizeof(self.elf_pheader) + len(evilcode)
        self.elf_pheader.p_memsz = self.elf_pheader.p_filesz + 0x100

        elf_header_bytes = string_at(addressof(self.elf_header), sizeof(self.elf_header))
        elf_pheader_bytes = string_at(addressof(self.elf_pheader), sizeof(self.elf_pheader))
        cont = elf_header_bytes + elf_pheader_bytes + evilcode
        print(["0x" + format(byte, '02X') for byte in cont])
        print("[+] shellcode len: %d" % len(cont))
        with open(outf, 'wb') as f:
            f.write(cont)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, default=None)
    parser.add_argument('-o', type=str, default="shellcode.bin")
    args = parser.parse_args()

    builder = ElfBuiler()
    K = Ks(KS_ARCH_X86, KS_MODE_64)
    with open(args.i, "r") as inf:
        asm_code = inf.read()
    print(asm_code)
    shellcode, err = K.asm(asm_code, as_bytes=True)
    assert err != 0
    builder.generate_elf(shellcode, args.o)
