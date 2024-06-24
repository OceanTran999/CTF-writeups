![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/80a64394-1404-4f1b-b712-6ce16f36a110)


It seems that they use the program in the previous challenge, the difference is they remove the `show_flag()`. Therefore we need to obtain the shell from the target server to get the flag ~~.

![file_checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/cfeb22a4-979f-4951-9313-2ad161992b51)


The program gives us the address of `printf()` as a hint and the `libc.so.6` file, using these we can easily check the `LIBC` version that the server's using. Also, we can calculate the address of `LIBC Base`, to calculate it I will let the address of `printf()` leaked from server minus to the address of `printf()` offset in `libc.so.6` file. Remember usually the address of `LIBC Base` will have the `0x00` in the last byte, therefore it can help us to recognize whether we are doing the right way or not.

![Libc_database](https://github.com/OceanTran999/CTF-writeups/assets/100577019/3eecdbb3-e811-4d0d-bff6-d89bd0a6d4b3)

Great!!! We know the version of `LIBC` and we can use `ret2libc` technique to exploit. I've already drawn the stack for this technique:

![Stacck](https://github.com/OceanTran999/CTF-writeups/assets/100577019/236a27bb-b9db-4aca-b4d7-6d5c33e9ce17)


Uh oh..... It seems I can't use this technique to get the shell...... But when I looks at the challenge again, I see they mention about `ROP (Return Oriented Programming)` :). So I decide to change technique, first let's find some usefull gadgets to exploit this technique, the program does not have gadgets for us, but luckily, the `libc.so.6` does.

![pop_rdi](https://github.com/OceanTran999/CTF-writeups/assets/100577019/1bfaea0c-f305-4caf-96d9-c64134f9cb9a)


![ret](https://github.com/OceanTran999/CTF-writeups/assets/100577019/41c6a0db-2985-4f31-a9b6-a1f20466a667)


After finding those gadgets, we just need to use this technique and obtain the shell to get the flag.

![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/b334ce3a-252c-4c57-971a-388071d6dd70)
