# Get the sword

![Chal](https://github.com/user-attachments/assets/f1e99dce-dbae-4989-86d0-eff91baf7c9c)


Here's the protection of this file

![Checksec](https://github.com/user-attachments/assets/652ac2af-cdc7-4dc0-9c49-c33255263258)


Here's the function that we can input.

![intro_func](https://github.com/user-attachments/assets/fed577a6-df93-424e-a6e2-57da12bb16cb)


In this challenge, the `win function` is `getSword()`.

![Win_func](https://github.com/user-attachments/assets/1434d88c-ef26-4d28-b5cb-b1f0c79d0ac7)


The input function uses the `scanf` with `%s` format string, which we can easy use buffer overflow attack because `scanf` reads until it receives the null byte.

![format_s](https://github.com/user-attachments/assets/456eb8ff-44d5-4cd6-9a22-113cd018478d)


So here's the stack I draw for this challenge.

![stack](https://github.com/user-attachments/assets/24e9de87-b5f6-4e02-84da-089337741e0f)


Now we just need the address of the `win` function to get the flag

![win_addr](https://github.com/user-attachments/assets/01d852f5-a7ad-4f29-ad72-77fa92f0c877)


![flag](https://github.com/user-attachments/assets/6bf5d3e4-bf19-433d-9b1a-289910ff5483)


# Dragon Secret Scroll

![Chal](https://github.com/user-attachments/assets/ed859a27-c6e7-44e1-b8f0-2b556b3171da)


In this challenge, it doesn't give me the binary file to exploit in local. Therefore I have to exploit directly in the remote server. The simplest technique I think to solve this challenge is format string vulnerability, so I try to test the input to see if it really works with the format string attack.

![Test_formatstr](https://github.com/user-attachments/assets/59fe449a-f3bc-4aa7-8a62-01b288bd43ca)


Yeah :) It really has format string vulnerability. Now, the format of the flag is `KCTF{flag}`, which in ASCII will be:
```
  4b:    K
  43:    C
  54:    T
  46:    F
```

So, I will find the position of output to see if there're hex values of this. Remember for the little endian.

![flag_position](https://github.com/user-attachments/assets/208ce68f-8ef0-429a-a224-c105aaee2b13)


Great!!! It's in the 6th position of output. Copy and paste to the Hex to String Converter online, this is the flag. So I just write the script to convert to these hex values into big endian and get the flag.

![hex_to_str](https://github.com/user-attachments/assets/88699867-463f-4693-ac09-f9927ec7d25b)


![convert_little_end](https://github.com/user-attachments/assets/cb9f4daa-75e7-42dc-9c4c-fdeb71e14147)


![Flag](https://github.com/user-attachments/assets/31ef82b9-58d8-47c9-b814-5c7b0f11b13b)


# win...win...Windows

![Chal](https://github.com/user-attachments/assets/982ed3b7-855b-49f2-b63a-f0b9a7ab1884)


![checksec](https://github.com/user-attachments/assets/bc048373-45ea-4845-bb75-c94ed9a60170)


The excutable file only has NX flag, which we can't execute the shell in the stack. In the `main()`, we see there's a vulnerability due to the `get()`, which can occur buffer overflow attack.

![main_func](https://github.com/user-attachments/assets/cbb5fe5c-b886-48b9-87d9-f8bf21de5f94)


The `win` function will give the shell for us. Now we need to make the program point to it.

![win_func](https://github.com/user-attachments/assets/ff28e372-1645-47a2-9718-94df26bc216d)


We can use buffer overflow attack to redirect to the win function. First we need to know the address of the `win`.

![win_addr](https://github.com/user-attachments/assets/6f813ac0-5502-490d-86dc-e0e292d3d78c)


Finally, draw the stack and get the flag.

![stack](https://github.com/user-attachments/assets/58a85e74-48ec-49b9-b84a-652295a4925e)


![Flag](https://github.com/user-attachments/assets/631d27bf-ddb1-4c1f-8ccc-23898d841883)
