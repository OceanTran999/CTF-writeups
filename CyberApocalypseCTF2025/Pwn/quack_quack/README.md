![Chal](https://github.com/user-attachments/assets/9ec57abd-0ad2-4631-bf8d-66d9993ede17)


![check_file](https://github.com/user-attachments/assets/954c7bac-36bd-4079-9317-955583b805cd)


The file doesn't have only `PIE` protection, so it's easier to interact with address of functions, testing the program, I see that the program will print the string after the `Quack Quack` in the user's input. The program has `Canary` right? So what if, I overwrite the program and put the `Quack Quack` near to the canary's value? Will it be leaked? The answer is yes, after leaking the canary we will overwrite the `$RIP` with address of `win()` and get the flag

![test](https://github.com/user-attachments/assets/b17a1519-e448-4061-a2fc-1c2b5f553897)



![Flag](https://github.com/user-attachments/assets/3856b999-90ca-4e77-9c60-5e000056feab)
