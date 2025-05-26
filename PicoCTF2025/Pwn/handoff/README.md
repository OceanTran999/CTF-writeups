![chal](https://github.com/user-attachments/assets/fc4c839b-e4a9-4538-aec5-992c0ea5a0d7)


The binary doesn't have any protection, so my first thought is put the shellcode in the stack and make the `$RIP` point to it.

![checksec](https://github.com/user-attachments/assets/6257bc50-10e6-49ad-92d8-dfa65551f162)


And I see that there's a buffer overflow vulnerabilty when we use the choice `3`.

![code2](https://github.com/user-attachments/assets/bba9b6ee-0ceb-4ad9-8f50-45febd60e7a7)


![run](https://github.com/user-attachments/assets/60de7521-2b04-4dac-8dc1-b382f9117780)


Also, we have 32 bytes input in choice `2`, which we can put the shellcode in this.

![code](https://github.com/user-attachments/assets/955321e3-9681-4db4-a9d5-3b6f0e677348)


When we input before exiting, using `gdb`, we see that the value of `$rax` always point to the first address of our input, so we will find the gadgets that relate to `$rax`. The `jmp $rax` is the suitable one. Therefore, the idea is we will create some assembly codes that make the `$rsp` point to the variable that contents shellcode. To run these assembly codes, we have to put them in the first input of choice `3` and use the gadget `jmp $rax` to make `$rsp` point to our assembly code, and finally point to the shellcode to get the shell.

![gdb](https://github.com/user-attachments/assets/ffeca99b-12af-4a15-b140-e47aaf54b8b5)


![flag](https://github.com/user-attachments/assets/74092410-7109-4370-ae09-edec3dccdcd2)
