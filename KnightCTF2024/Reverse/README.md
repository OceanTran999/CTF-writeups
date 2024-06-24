> **_NOTE:_**  In Reverse Engineer challenges, I usually change the name, value of variables and functions to make the solution easier.

# Dragon Binary

![chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/be1da94f-87af-4763-b32f-8720325f7b83)


In this challenge, I don't see any calculation or modifying the passcode, so I think it may be just input the correct passcode. I find the value which converts in little endian will be `letMeIn`. When I try to input it really the passcode :) .

![string](https://github.com/OceanTran999/CTF-writeups/assets/100577019/22794a4d-49aa-4aaa-8c71-2767c7a43dfe)


![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/94162f74-b821-409e-93ca-a8482826a40d)


# Knight Armoury

![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/f2dc2492-f9fd-4974-979e-ce40a2ac5fbe)


In this challenge, the `win` function will be `func1()`, which it checks if the pass key we input is correct, it will give us the flag.

![Func1](https://github.com/OceanTran999/CTF-writeups/assets/100577019/34d7ea9a-354b-424f-859a-b964fb9b0a37)


Before calling the `func1()`, it will call the `func2()` first, and handle the passkey with `func4()` and `func3()`. So we just need to know how the `func3()` and `func4()` handle the pass key, we will get the flag.

![Func2](https://github.com/OceanTran999/CTF-writeups/assets/100577019/b1c09413-7ee8-42a0-8321-4fe0328143dd)


![Func3](https://github.com/OceanTran999/CTF-writeups/assets/100577019/27f46e7e-11a0-4101-877d-32cb5f2c30db)


![Func4](https://github.com/OceanTran999/CTF-writeups/assets/100577019/4159a504-a795-4a8e-b3fe-7c62c2c4bfec)


In `func3()` and `func4()`, it handles each characters in the pass key, if the character is in `A-Z`, it will computes different the `a-z`. Knowing this, we just write the script and printing the final pass key to get the flag.

![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/a3b5bb27-3164-4e8a-9595-dee6b40cde49)
