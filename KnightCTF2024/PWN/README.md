# Get the sword

![Chal](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/58ebf417-c481-4dd5-8ea2-7924605ba4d2)


Here's the protection of this file

![Checksec](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/cd927a4a-3692-4514-81f4-9c184fb79698)


Here's the function that we can input.

![intro_func](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/6a7433a3-462b-4abf-a0f2-ae935020c8a5)


In this challenge, the `win function` is `getSword()`.

![Win_func](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/14ea1790-72e8-40cb-86e2-d7736c0f0835)


The input function uses the `scanf` with `%s` format string, which we can easy use buffer overflow attack because `scanf` reads until it receives the null byte.

![format_s](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/53e2c5e7-82ba-4eee-aafb-88d97818e314)


So here's the stack I draw for this challenge.

![stack](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/bf3b9979-c2dd-4845-ace7-9447c8ee0ceb)


Now we just need the address of the `win` function to get the flag

![win_addr](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/310b4c17-a3a7-4a5b-ae02-836dfec10d7d)


![flag](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/91dea3af-4d03-4864-8044-efb8fe58895f)


# Dragon Secret Scroll

![Chal](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/151509c8-c4a5-47ac-ae4d-7013fc4fde17)


In this challenge, it doesn't give me the binary file to exploit in local. Therefore I have to exploit directly in the remote server. The simplest technique I think to solve this challenge is format string vulnerability, so I try to test the input to see if it really works with the format string attack.

![Test_formatstr](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/8cfbcbf2-07a5-4b2d-9eb9-2eda34bbd422)


Yeah :) It really has format string vulnerability. Now, the format of the flag is `KCTF{flag}`, which in ASCII will be:
```
  4b:    K
  43:    C
  54:    T
  46:    F
```

So, I will find the position of output to see if there're hex values of this. Remember for the little endian.

![flag_position](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/5613367b-18b9-4736-a9c7-b658d02012b9)


Great!!! It's in the 6th position of output. Copy and paste to the Hex to String Converter online, this is the flag. So I just write the script to convert to these hex values into big endian and get the flag.

![hex_to_str](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/c71424c8-fefd-4dc7-9860-6a1e555dd60b)


![convert_little_end](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/8ecad809-93b3-47dd-a19c-f7fdaf1fa2c8)


![Flag](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/b1158b2b-11ef-4895-b75e-1a56ad30b750)


# win...win...Windows

![Chal](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/d1808009-e4cd-4a98-b206-b1ede64ff3a1)


![checksec](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/28b8fc8a-b820-49b9-8a80-f3ce1007b18e)


The excutable file only has NX flag, which we can't execute the shell in the stack. In the `main()`, we see there's a vulnerability due to the `get()`, which can occur buffer overflow attack.

![main_func](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/a95c8a43-dd14-49a4-84a0-bd7c0d3168fc)


The `win` function will give the shell for us. Now we need to make the program point to it.

![win_func](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/fca89470-a0c3-4f8a-9ac0-0bb41adc1ede)


We can use buffer overflow attack to redirect to the win function. First we need to know the address of the `win`.

![win_addr](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/51fde572-1b7b-4fbc-87c4-a4eaec3138e9)


Finally, draw the stack and get the flag.

![stack](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/0c297c8c-ec91-448f-a642-248dc6b78f3f)


![Flag](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/6ae216c0-2724-4504-b574-5984f0929205)
