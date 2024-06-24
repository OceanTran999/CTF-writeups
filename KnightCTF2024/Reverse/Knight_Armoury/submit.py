from pwn import remote, process, log

def solve(boolean):
    if boolean:
        r = remote('198.58.104.183', 11337)
    else:
        r = process('./knight_armoury')
    
    str_check = 'IaMaKnight'         #'thginKaMaI'
    password1 = ''
    for i in range(len(str_check)):
        if(ord(str_check[i]) <= 96 or ord(str_check[i]) > 122):
            if(ord(str_check[i]) > 64 and ord(str_check[i]) <= 90):
                value = (ord(str_check[i]) - 52) % 26 + 65
        else:
            value = (ord(str_check[i]) - 84) % 26 + 97

        password1 += chr(value)
    log.success(f"First password is: {password1}")

    password2 = ''

    for i in range(len(password1)):
        if(ord(password1[i]) <= 96 or ord(password1[i]) > 122):
            if(ord(password1[i]) > 64 and ord(password1[i]) <= 90):
                value = (ord(password1[i]) - 65 + 3) % 26 + 65
        else:
            value = (ord(password1[i]) - 97 + 3) % 26 + 97

        password2 += chr(value)    
    log.success(f"Final password is: {password2}")

    r.sendline(password2)
    r.interactive()

solve(True)