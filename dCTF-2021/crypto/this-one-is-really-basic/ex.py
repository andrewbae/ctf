#!/usr/bin/env python3

import base64

flag = open("./cipher.txt", "r").read()

for v0 in range(42):
    flag = base64.b64decode(flag)

print(flag)
