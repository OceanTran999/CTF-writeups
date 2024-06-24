# Get the sword

![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/7ee52fc4-c9f1-4a82-b532-bfd198f0c2da)


Here's the protection of this file

![Checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/67d4b075-4201-4c48-84e2-9fd9b354c797)


Here's the function that we can input.

![intro_func](https://github.com/OceanTran999/CTF-writeups/assets/100577019/2182ed71-a63f-4312-b698-35be65d2d334)


In this challenge, the `win function` is `getSword()`.

![Win_func](https://github.com/OceanTran999/CTF-writeups/assets/100577019/1f6e32a8-4ba9-4117-8c38-805b267fc530)


The input function uses the `scanf` with `%s` format string, which we can easy use buffer overflow attack because `scanf` reads until it receives the null byte.

![format_s](https://github.com/OceanTran999/CTF-writeups/assets/100577019/50dab4ce-0988-4137-9685-15ea25eb6dc6)


So here's the stack I draw for this challenge.

![stack](https://github.com/OceanTran999/CTF-writeups/assets/100577019/a7342d0b-559b-421f-9fff-1faa087118ae)


Now we just need the address of the `win` function to get the flag

![win_addr](https://github.com/OceanTran999/CTF-writeups/assets/100577019/cb6db636-2db7-471d-b847-251e870e1ab6)


![flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/82de6ad4-ed7d-4320-bb30-a4aa4d314335)


# Dragon Secret Scroll

![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/5f8cc684-2bef-49b9-9626-fd28f7ff2074)


In this challenge, it doesn't give me the binary file to exploit in local. Therefore I have to exploit directly in the remote server. The simplest technique I think to solve this challenge is format string vulnerability, so I try to test the input to see if it really works with the format string attack.

![Test_formatstr](https://github.com/OceanTran999/CTF-writeups/assets/100577019/b9b47cc9-a899-4a7f-a840-9da10fcf6586)


Yeah :) It really has format string vulnerability. Now, the format of the flag is `KCTF{flag}`, which in ASCII will be:
```
  4b:    K
  43:    C
  54:    T
  46:    F
```

So, I will find the position of output to see if there're hex values of this. Remember for the little endian.

![flag_position](https://github.com/OceanTran999/CTF-writeups/assets/100577019/30011e83-1a9e-4bcf-84a9-9216b786cf69)


Great!!! It's in the 6th position of output. Copy and paste to the Hex to String Converter online, this is the flag. So I just write the script to convert to these hex values into big endian and get the flag.

![hex_to_str](https://github.com/OceanTran999/CTF-writeups/assets/100577019/6b18cd33-a391-40b2-8f29-9d98fe9c8d43)


![convert_little_end](https://github.com/OceanTran999/CTF-writeups/assets/100577019/7b653f25-4efd-4a29-8e95-017e3b427ba9)


![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/c9c26b97-9a78-4ece-b56f-4f43c576b998)


# win...win...Windows

![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/838614e2-264d-40e1-9290-2b06caf807e7)


![checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/d9a5fee9-4024-4cca-bce6-44584d7bc15b)


The excutable file only has NX flag, which we can't execute the shell in the stack. In the `main()`, we see there's a vulnerability due to the `get()`, which can occur buffer overflow attack.

![main_func](https://github.com/OceanTran999/CTF-writeups/assets/100577019/01273e68-8a72-490d-9dd5-67b964a813cd)


The `win` function will give the shell for us. Now we need to make the program point to it.

![win_func](https://github.com/OceanTran999/CTF-writeups/assets/100577019/a5eac460-203f-49bf-b6d2-fb7cdba260f6)


We can use buffer overflow attack to redirect to the win function. First we need to know the address of the `win`.

![win_addr](https://github.com/OceanTran999/CTF-writeups/assets/100577019/8d363391-3dac-47b9-b0a6-06187386c7f3)


Finally,  the stack and get the flag.

![stack](https://github.com/OceanTran999/CTF-writeups/assets/100577019/878d9881-3fa4-4bcc-9289-b49c37d3c4b0)


![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/f3e609c2-31dc-4863-a264-8d1f5ff11d3b)
