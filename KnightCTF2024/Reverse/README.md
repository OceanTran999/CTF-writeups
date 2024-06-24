> **_NOTE:_**  In Reverse Engineer challenges, I usually change the name, value of variables and functions to make the solution easier.

# Dragon Binary

![chal](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/4217ec80-bf52-440c-a12f-8d3c2bdf5346)


In this challenge, I don't see any calculation or modifying the passcode, so I think it may be just input the correct passcode. I find the value which converts in little endian will be `letMeIn`. When I try to input it really the passcode :) .

![string](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/6307d16f-fa31-4ac0-a54e-76c3806b7a52)


![Flag](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/f9207167-42ff-43b1-9867-c8438de353c6)


# Knight Armoury

![Chal](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/73d65f08-81b3-449b-8a34-b08bea566971)


In this challenge, the `win` function will be `func1()`, which it checks if the pass key we input is correct, it will give us the flag.

![Func1](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/c9120685-e758-43e8-9444-6a6cb7da9943)


Before calling the `func1()`, it will call the `func2()` first, and handle the passkey with `func4()` and `func3()`. So we just need to know how the `func3()` and `func4()` handle the pass key, we will get the flag.

![Func2](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/cc5c83c8-3ce3-4ac0-b48b-f85a231264ef)


![Func3](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/e75ec14c-d3e3-4478-ae57-c567bd6e4cb0)


![Func4](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/9ed27fc1-c26d-43f1-b6db-9f2600148124)


In `func3()` and `func4()`, it handles each characters in the pass key, if the character is in `A-Z`, it will computes different the `a-z`. Knowing this, we just write the script and printing the final pass key to get the flag.

![Flag](https://github.com/OceanTran999/KnightCTF2024/assets/100577019/7123f734-6c17-4f38-92fa-f363872b9470)
