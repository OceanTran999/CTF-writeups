![checksec](https://github.com/user-attachments/assets/5f3d66fb-f24a-4c0c-a265-603924eef238)


The program only has `NX enabled` which we can't execute the shellcode in the stack, but there's no canary and PIE, so we can hope there's a buffer overflow vulnerability to exploit.

![gdb](https://github.com/user-attachments/assets/76036975-41f8-42fa-b5d3-c84653ca0b45)


Using `gdb` I found that the program use `gets()` for giving input, which makes a buffer overflow vulnerability here. Perfect, now we just need to find some gadgets for making a ROP chain and get the shell ;)

![buff_over_detected](https://github.com/user-attachments/assets/a75fb623-0044-45ab-93d3-75fba95d1f2d)


![pop_rdi](https://github.com/user-attachments/assets/a3f037d8-1a69-4a15-ada5-e475efd06192)


![flag](https://github.com/user-attachments/assets/baddd625-18c0-4543-89ed-8b8286030b68)
