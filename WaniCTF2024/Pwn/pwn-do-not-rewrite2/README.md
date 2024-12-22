![Chal](https://github.com/user-attachments/assets/8f871d10-1167-4dfa-b3d9-e0d1e3e90fc8)


![file_checksec](https://github.com/user-attachments/assets/d4836dbc-b06e-41f6-9514-44487700900d)


It seems the challenge is the same as the previous, but this time it doesn't give the win() function. So, same technique, I just then use the `ROP` technique to know the version of `LIBC` that the target server is using, finally find the suitable offset and execute the `system('/bin/sh')` to get the shell. So here's the stack I wrote after getting the libc version
![Stacck](https://github.com/user-attachments/assets/f582e167-b06b-41b2-925a-f213f16971ec)


To make a ROP chain attack, first we need to find the address of suitable gadget using `ROPgadget` tool.

![ret](https://github.com/user-attachments/assets/94758847-a167-477b-af28-1b437fe69c0e)


![pop_rdi](https://github.com/user-attachments/assets/cee5cb70-6618-4840-a1f5-489a029121d6)


After leaking address of some function, searching libc database to get the version of LIBC.

![Libc_database](https://github.com/user-attachments/assets/7c965d2f-6116-4994-9d32-b12e473e6cc2)


![Flag](https://github.com/user-attachments/assets/13afc9bb-88b5-45ef-9614-824104d1200c)
