from ctypes import Structure
from ctypes import c_int64, c_uint64
from ctypes import c_int32, c_uint32
from ctypes import c_int16, c_uint16
from ctypes import c_ubyte

"""
/* Type for a 16-bit quantity.  */
typedef uint16_t Elf32_Half;
typedef uint16_t Elf64_Half;

/* Types for signed and unsigned 32-bit quantities.  */
typedef uint32_t Elf32_Word;
typedef	int32_t  Elf32_Sword;
typedef uint32_t Elf64_Word;
typedef	int32_t  Elf64_Sword;

/* Types for signed and unsigned 64-bit quantities.  */
typedef uint64_t Elf32_Xword;
typedef	int64_t  Elf32_Sxword;
typedef uint64_t Elf64_Xword;
typedef	int64_t  Elf64_Sxword;

/* Type of addresses.  */
typedef uint32_t Elf32_Addr;
typedef uint64_t Elf64_Addr;

/* Type of file offsets.  */
typedef uint32_t Elf32_Off;
typedef uint64_t Elf64_Off;

/* Type for section indices, which are 16-bit quantities.  */
typedef uint16_t Elf32_Section;
typedef uint16_t Elf64_Section;

/* Type for version symbol information.  */
typedef Elf32_Half Elf32_Versym;
typedef Elf64_Half Elf64_Versym;
"""
ElfN_Half = c_uint16
ElfN_Word = c_uint32
ElfN_Sword = c_int32
ELFN_Xword = c_uint64
ELFN_Sxword = c_int64
ELFN_Section = c_uint16
ElfN_Versym = c_uint16
ElfN_Addr = c_uint64
ElfN_Off = c_uint64


class ElfN_Ehdr(Structure):
    EI_NIDENT = 16
    _pack_ = 1
    _fields_ = [
        ("e_ident", c_ubyte * EI_NIDENT),
        ("e_type", ElfN_Half),
        ("e_machine", ElfN_Half),
        ("e_version", ElfN_Word),
        ("e_entry", ElfN_Addr),
        ("e_phoff", ElfN_Off),
        ("e_shoff", ElfN_Off),
        ("e_flags", ElfN_Word),
        ("e_ehsize", ElfN_Half),
        ("e_phentsize", ElfN_Half),
        ("e_phnum", ElfN_Half),
        ("e_shentsize", ElfN_Half),
        ("e_shnum", ElfN_Half),
        ("e_shstrndx", ElfN_Half)
    ]


class Elf64_Ehdr(Structure):
    EI_NIDENT = 16
    _pack_ = 1
    _fields_ = [
        ("e_ident", c_ubyte * EI_NIDENT),
        ("e_type", ElfN_Half),
        ("e_machine", ElfN_Half),
        ("e_version", ElfN_Word),
        ("e_entry", ElfN_Addr),
        ("e_phoff", ElfN_Off),
        ("e_shoff", ElfN_Off),
        ("e_flags", ElfN_Word),
        ("e_ehsize", ElfN_Half),
        ("e_phentsize", ElfN_Half),
        ("e_phnum", ElfN_Half),
        ("e_shentsize", ElfN_Half),
        ("e_shnum", ElfN_Half),
        ("e_shstrndx", ElfN_Half)
    ]


class ElfN_Phdr(Structure):
    _pack_ = 1
    _fields_ = [
        ("p_type", ElfN_Word),
        ("p_flags", ElfN_Word),
        ("p_offset", ElfN_Off),
        ("p_vaddr", ElfN_Addr),
        ("p_paddr", ElfN_Addr),
        ("p_filesz", ElfN_Off),
        ("p_memsz", ElfN_Off),
        ("p_align", ElfN_Off)
    ]


class Elf64_Phdr(Structure):
    _pack_ = 1
    _fields_ = [
        ("p_type", ElfN_Word),
        ("p_flags", ElfN_Word),
        ("p_offset", ElfN_Off),
        ("p_vaddr", ElfN_Addr),
        ("p_paddr", ElfN_Addr),
        ("p_filesz", ElfN_Off),
        ("p_memsz", ElfN_Off),
        ("p_align", ElfN_Off)
    ]
