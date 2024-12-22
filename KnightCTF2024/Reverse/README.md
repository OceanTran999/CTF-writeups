> **_NOTE:_**  In Reverse Engineer challenges, I usually change the name, value of variables and functions to make the solution easier.

# Dragon Binary

![chal](https://github.com/user-attachments/assets/bce36776-e066-4c9d-baac-4205ed79cb0c)


In this challenge, I don't see any calculation or modifying the passcode, so I think it may be just input the correct passcode. I find the value which converts in little endian will be `letMeIn`. When I try to input it really the passcode :) .

![string](https://github.com/user-attachments/assets/982451ad-5f0c-4de1-b901-8b97b35b452c)


![Flag](https://github.com/user-attachments/assets/1607fa3b-8c84-4554-9c38-6747b4eb0674)


# Knight Armoury

![Chal](https://github.com/user-attachments/assets/e5aab340-638e-416b-b4fe-792f9d2280b9)


In this challenge, the `win` function will be `func1()`, which it checks if the pass key we input is correct, it will give us the flag.

![Func1](https://github.com/user-attachments/assets/d14b6b13-f5cd-4292-8501-dc1cab53401b)


Before calling the `func1()`, it will call the `func2()` first, and handle the passkey with `func4()` and `func3()`. So we just need to know how the `func3()` and `func4()` handle the pass key, we will get the flag.

![Func2](https://github.com/user-attachments/assets/7eb73887-0c06-4f08-b3b7-e4e86efe8f96)


![Func3](https://github.com/user-attachments/assets/63ee311e-1931-4380-98ee-41f85ca414fc)


![Func4](https://github.com/user-attachments/assets/2e54893a-43da-41ec-ab9d-8c06676724bc)


In `func3()` and `func4()`, it handles each characters in the pass key, if the character is in `A-Z`, it will computes different the `a-z`. Knowing this, we just write the script and printing the final pass key to get the flag.

![Flag](https://github.com/user-attachments/assets/61969001-c2b8-4e75-bdd9-0064a91672a7)
