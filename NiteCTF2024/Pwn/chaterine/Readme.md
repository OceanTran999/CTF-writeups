![Chal](https://github.com/user-attachments/assets/8063b18c-530f-4689-b146-e4ff04c53dfe)

# My solution
The binary doesn't have the Canary protect, so will it be the buffer overflow attack?

![checksec](https://github.com/user-attachments/assets/4c47a57c-d03b-4b9b-a3cf-4b5409a92fab)


Using `gdb`, I see the challenge is the `ret2win` challenge.

![target_systemfunc](https://github.com/user-attachments/assets/b741f35e-9205-485e-b0ff-7cd2b770bf03)

Using IDA, after a little bit reversing, I understand that the first input will allow us any value except `spiderdrive`, but to obtain the shell, we have to overwrite it somehow to win this.

![IDA_pro_getshell](https://github.com/user-attachments/assets/4402eafe-7c48-4f35-9d2d-d4b383517195)


Also, there're 2 format string vulnerabilities of 2 inputs, so we can abuse this to exploit.

![fmtstr2](https://github.com/user-attachments/assets/daa5d75a-aeb1-43eb-bf22-4370b84b30d1)


![test2](https://github.com/user-attachments/assets/7024a042-c7ec-4d20-aed8-12039c77c89c)


![test](https://github.com/user-attachments/assets/6aedd149-9de6-4f08-9f8a-0bd62d1d19ef)


![fmtstr](https://github.com/user-attachments/assets/b4ff5670-ff20-4d26-ba32-ea8b286ffae8)


Using the 2nd input, I see that in the 12th position (LOCAL), it has the stack address, using `gdb` to check the `$rbp` address.

![stack_addr](https://github.com/user-attachments/assets/e9468d74-5f61-46f5-81ca-5ea50188bc9a)


![rbpaddr](https://github.com/user-attachments/assets/7a2f8966-37e8-4d74-96bb-2d62721fd614)


Hmmmm, if the offset of these address doesn't change in different runtime, I will use this to get the address of the **1st input**.

![stack_addr2](https://github.com/user-attachments/assets/3ab5480c-e57e-4a7b-a3e6-89e059d8e889)


![rbpaddr2](https://github.com/user-attachments/assets/6354724e-1632-4398-93bb-ec89bc0e2c4b)


And great, it doesn't change, using `Double Free` or `UAF` to make the chunk point to the stack which the **1st input** is locating, and finally change it with `spiderdrive` value and get the shell ;).

![malloc_error](https://github.com/user-attachments/assets/3c237c6f-c7d2-4ccc-a7cb-95a2e419449a)


But nahhh, the program has the aligned tcache check, so I can't make the chunk to point to the stack LOL.

# Final solution
Asking in the Discord for help (Of course after the competition), I realize that they use modern version Libc. The version they are using is GLIBC-2.35 I think. Therefore, to solve this, I just get the address of the chunk I am using, the stack address using `%p` for 1st input, calculate them with `<stack_address> ^ <heap_chunk_address> >> 12`, we will use the final value to make the `chunk->next` point to the place we want.

![discord_help](https://github.com/user-attachments/assets/885a8ed3-8029-421c-9267-11a4e09a45e4)


Checking again with `gdb`, I see that now I am pointing to the 1st input of the program, now just get the shell and win the game.

![gdb](https://github.com/user-attachments/assets/d6091e4b-71e9-4aa1-ae84-f9a00582f06e)


![shell_local](https://github.com/user-attachments/assets/76357bfc-124d-41ba-9946-a6f174ced008)


The another factor that makes me feel complicated is that the offset of target server and my local is totally different due to the OS and GLIBC, so if I know the bypass tcache check I still couldn't solve this right 🤡?

![flag](https://github.com/user-attachments/assets/8bff39c0-7cbd-42f1-a19d-5e1e26b5a2e7)
