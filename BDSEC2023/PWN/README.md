# anyaForger
First, let's see type of file, I saw this is ELF32 file.

![readelf](https://github.com/OceanTran999/CTF-writeups/assets/100577019/6d91fa3b-6942-4604-adda-8be06426657f)

Therefore, I would use IDAPro 32-bits to see the full source code of this file. And here is `main()` and `vuln()`:

![mainFunc](https://github.com/OceanTran999/CTF-writeups/assets/100577019/79764ab9-e998-4368-ac23-e2da749de9ea)

![vulnFunc](https://github.com/OceanTran999/CTF-writeups/assets/100577019/0ba7aaf2-873c-47c8-adb4-49b4f1e3d8c3)

Then I checked the protection of this file. As the result, the file had no protection.

![checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/5348865f-79c1-4744-ac6e-4216e81583b0)

Next, we will `disassemble vuln`:

I suddenly saw `mov  DWORD PTR [ebp - 0xc], 0x123456678`. Therefore I considered that the address of variable "v1" will be `ebp-0xc`

![v1](https://github.com/OceanTran999/CTF-writeups/assets/100577019/24d0731f-7c79-4ef6-9fb2-e61999368a11)

Next, before call the `gets()` function, I saw there was a code: `lea  eax, [ebp-0x2c]`. Therefore I thought the address of gets() function will be `ebp-0x2c`

![gets](https://github.com/OceanTran999/CTF-writeups/assets/100577019/562cf9dc-327c-4304-8a81-293545491491)

After that, I saw the address `ebp-0xc` compare with the value `0xdeadbeef`. So, I realized that I had to overwrite the v1 value to get the flag.

![deadbeef](https://github.com/OceanTran999/CTF-writeups/assets/100577019/e79adaa8-67f3-41ab-b8fd-e1c091608ccd)

Here is my stack that I drew it.

![stack](https://github.com/OceanTran999/CTF-writeups/assets/100577019/54f1cac0-c7da-4bba-bc2e-5221ce9cb805)

Wakuwaku~~ I finally got the flag

![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/1fe54231-de58-4c33-80b4-0d80897e4c43)

_**Sadly :( these 2 beneath challenges I didn't have time to solve, but I was able to solve it after the competition XD**_

# callme
Type of file:

![readelf](https://github.com/OceanTran999/CTF-writeups/assets/100577019/70c30247-e586-4ae6-b044-5aa117902221)

Used IDAPro 32-bits, I got source code. Here's the `main()` function

![mainFunc](https://github.com/OceanTran999/CTF-writeups/assets/100577019/bd3ac178-88e1-4986-bbc4-a1c34036a720)

![mainFunc_2](https://github.com/OceanTran999/CTF-writeups/assets/100577019/8d9bbc72-d107-4e86-a54c-b00d7bd58c62)

Check the file's protection:

![checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/e778eaa2-bec7-493f-b8e2-3a379a1f834f)

Then I `disassemble main`. And did as same as the _**AnyaForger**_ challenge

![scanf](https://github.com/OceanTran999/CTF-writeups/assets/100577019/f657b714-b370-4632-bf2e-ec12aa686636)

![test](https://github.com/OceanTran999/CTF-writeups/assets/100577019/4e6e4a98-8eb8-4b76-8e9c-4cd77349615b)

Finally, I got stack like this:

![stack](https://github.com/OceanTran999/CTF-writeups/assets/100577019/91da1ba5-04b2-4c51-b732-f7d71de6ab73)

Booom!!!! I got the flag. EZPZ

![flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/6c7d697c-16f2-45c0-9543-f018c09ecb70)


# ghost
Here we got the protections

![checksec](https://github.com/OceanTran999/CTF-writeups/assets/100577019/57614669-fe12-4687-8b59-b9dd12b14ba6)

Then I check the type of file and it is the ELF 64-bits

![readelf](https://github.com/OceanTran999/CTF-writeups/assets/100577019/81118fb6-af0a-431e-bd55-489d239b8c5e)

Therefore, I had to use IDAPro 64-bits to observe the source code. Here's the `main()` function:

![SourceCode](https://github.com/OceanTran999/CTF-writeups/assets/100577019/9b7ed5a0-fcf9-4c92-96dc-19e7959fa231)

Did as same as those 2 above challenges. I got the stack like this:

![stack](https://github.com/OceanTran999/CTF-writeups/assets/100577019/aea8a641-19d4-47ce-a95b-c1dba4dcf986)

Finally, submit to server and I got the flag. Yayyyyy :D

![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/2e72aeff-bd9a-4d0b-851a-4ccd608423b9)
