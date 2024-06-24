![chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/685248fe-ebaa-4234-8438-1f033981495d)


Let's check file's protection:

![File_checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/bf5fd058-4978-440d-915a-5d3c61fdfc7f)


It seems that the program will change the address in the memory each time it's executed, we also can not execute the shellcode in the stack due to `NX` protection, and there's `Canary` to detect the buffer overflow attack. Looking at the source code that the challenge gives, it seems they show us the address of `show_flag()`, which is very suitable for us cause we don't have to worry about how to get the flag.

![Code](https://github.com/OceanTran999/CTF-writeups/assets/100577019/9e1acf0c-2b76-4eaa-b3a5-d11737d89403)


Running the program, it seems that we've made buffer overflow attack in spite of basic input.

![canary_detected](https://github.com/OceanTran999/CTF-writeups/assets/100577019/0912161f-0a62-4eee-b1fd-0f42d85b3f8d)


So I decide to use `gdb-peda` to debug the program, I will set 4 breakpoints which're after the `call scanf` and `call printf` instruction. It seems that each `Ingredient` object has 72 bytes length, you can see the `0x41414141`, `0x42424242` and `0x43434343` values I inputted with `Ingredient[1]`, `Ingredient[2]` and `Ingredient[3]` respectively. So the `Ingredient[4]` object is the main reason to cause the vulnerability, when we input the **calories per gram** of `Ingredient[4]`, we will modify the **Canary** value

![canary_modified](https://github.com/OceanTran999/CTF-writeups/assets/100577019/d4f13180-7fba-459b-99bb-17ab56e52a83)


The program also does not allow us to skip if we don't give it the input. Then.... How to bypass this? To solve this, we just need to input with `.`, the `scanf("%lf")` will skip it and the canary will not be changed. To make sure this is correct, I use `GDB` to debug again.

![check_dot](https://github.com/OceanTran999/CTF-writeups/assets/100577019/b0c628af-e8ce-43e1-8256-939701494f96)


And, the value of `Ingredient[4].name` will overwrite the return address, you can see that the `44444444` in the `$RIP` register, that is `DDDD` I inputted.

![RIP](https://github.com/OceanTran999/CTF-writeups/assets/100577019/c2c61b6b-588f-40b4-ac1a-2308c09fc487)


Great!!! We have all the information we have, now let's exploit.

![Excellent](https://github.com/OceanTran999/CTF-writeups/assets/100577019/4a637151-f711-448b-806c-72bc526e96a7)


We attached the `show_flag()` but the server does not give us the flag? Just modify the address inside `show_flag()`, and you will get the flag ;)

![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/0af990ff-dfa3-434c-8d90-f9b30ecfe8c4)
