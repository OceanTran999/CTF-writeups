![chal](https://github.com/user-attachments/assets/8f467842-90ee-4201-8bcf-1b19c6c1cdb6)

# My solution
This challenge only has `NX` protection which we can't execute the shellcode in the stack.

![checksec](https://github.com/user-attachments/assets/b64fce5c-b292-4651-911f-49902e27698a)


During reconnaissancing and debugging the binary, I saw that after giving the input, the `$RAX` register will be equal to the `<size_of_input> + 1`.

![input_and_RAX](https://github.com/user-attachments/assets/abab8f65-c5ac-4d5f-994b-e735d4209aed)


The program also has few gadgets to make a simple ROP chain attack...

![ropgadget](https://github.com/user-attachments/assets/74b229a2-bc88-4786-9f7c-6911cf582eb5)


Nonetheless, the program has the `gift()` which provide us the `syscall` gadget, so with this I can do the Sigreturn ROP(SROP) technique to exploit, rightt? Great. Let's do this technique and make the program be executable so that we can use `ret2shellcode` to get the remote shell. Therefore, I will need the `mprotect()` value, the base address of the program, the size of program to reset the permission, the pointer of `main()` function because it has the `vuln()` function inside and the address of `syscall` gadget.

![vmmap](https://github.com/user-attachments/assets/38d34efd-864b-4820-a326-4a20d07bddf2)


![pointer_of_main](https://github.com/user-attachments/assets/8fe94c9f-ebff-4594-9524-c7b3456e1edd)


Great, so using `gdb`, I see that we are doing the right way, make the program run again to execute the `rt_sigreturn()` syscall, after that execute the `mprotect()` to make the binary executable.

![gdb](https://github.com/user-attachments/assets/1dc5ee86-77e9-499e-adbb-d6199783afa0)


![gdb2](https://github.com/user-attachments/assets/5343e29b-e4ee-4749-8018-2945c8389903)


![gdb3](https://github.com/user-attachments/assets/9282c886-30a3-4411-8719-6e74e11741c5)


Sadly🥹, the program crashed but I didn't know why...
![Error](https://github.com/user-attachments/assets/84b232db-2222-4412-93a5-965883b9eb38)


After searching I see that `SIGSYS` means that the program is using `seccomp()`, which means it will block some critical functions such as `syscall`, `execve`, `mprotect()`, etc.
![stack_ovrflow](https://github.com/user-attachments/assets/991c507b-a269-42fc-af5f-a5c42a19e8f3)


Using IDA, I see the `prctl()` is calling the `seccomp()`.
![prctl](https://github.com/user-attachments/assets/81f6f34f-1d8e-4b3b-8920-28156e19f739)


![Seccomp](https://github.com/user-attachments/assets/1c45f3a4-8c47-40ec-a10c-c16073c6eb3d)


![Seccomp2](https://github.com/user-attachments/assets/5a4e82db-a013-431d-bbd8-29c83e301245)


# Final solution
Welp, there's a tool called `seccomp_tools` to check which function it will allow to execute in the binary, so after using it, I see that it allows `sendfile()`, which copy the content of a file descriptor to another file descriptor, such as STDOUT(fd=1)

![seccomp_tools](https://github.com/user-attachments/assets/213faa12-1f18-4e15-9795-4fec3c359ed8)


The most important thing I've just learnt during the CTF is that I have to run `docker` so that I can do the local exploit as same as I am dealing with remote. So, to know the file descriptor of `flag.txt`, after running the docker, I just need to use this tool....

![socat](https://github.com/user-attachments/assets/64832f23-51d6-44cf-8859-e1af5487a231)


And we get the flag.

![flag](https://github.com/user-attachments/assets/7ffc5373-055c-4d35-9558-b237022def11)
