![chal](https://github.com/user-attachments/assets/5bc84f8c-551b-4a07-9720-c48f5d08c1fe)


With `checksec` we can see that the binary file has all protection, it seems a very hard challenge I think...
![File_checksec](https://github.com/user-attachments/assets/c9c31ccd-7f30-44ab-bfb9-1b69c09626d7)


However, when reading the given source code, I realize that there's a buffer overflow vulnerability because the `ingredient[3]` has only 3 elements, while the `for` loop it gives 4 elements. Also, this challenge is `ret2win`, which gives us the address of flag function.


![Code](https://github.com/user-attachments/assets/fd6a58ab-aace-4fd7-a0bd-465446648670)


![canary_detected](https://github.com/user-attachments/assets/e8e6f535-f7f5-4f14-90b9-acd529b721e7)


Welp, it seems we are having problem with Canary, so how to handle with this? The inputs have 1 `char` and 2 `double`, when debugging I see that the `calories_per_gram` is at the Canary value, which is the type of `double` input. To bypass this, I just give the `.` input so it will pass the Canary without overwriting it. Finally, we will use the address of flag to overwrite the `$RIP` with `char name[50]`.

![dot](https://github.com/user-attachments/assets/ac63d25c-3d3c-4250-9a7a-5ac4c16a3ec2)


`Segmentation fault` error means that I have overwritten the `$RIP` successfully. I use `gdb-peda` to debug the program and detect that `calories_per_gram` is the reason to overwrite the Canary value.

![canary_modified](https://github.com/user-attachments/assets/bf3e782e-064b-4331-a0c7-64d9309de84f)


And this is Canary value when I give the `.` input to `calories_per_gram`. Great, now just make the `$RIP` point to the win() and get the flag :p.

![check_dot](https://github.com/user-attachments/assets/664aec5e-6e3f-4d7a-9322-8abab5044a69)


![RIP](https://github.com/user-attachments/assets/9539e1a5-be43-442f-b5e1-7ab0f75a94e7)


![Excellent](https://github.com/user-attachments/assets/6f1ca997-4184-43a4-9b0a-c2fc6a950a1f)


![Flag](https://github.com/user-attachments/assets/05c05b24-e95d-43bd-8fd7-0137cef98cb8)
