# anyaForger
First, let's see type of file, I saw this is ELF32 file.

![readelf](https://github.com/OceanTran999/BDSEC2023/assets/100577019/0ec68262-df6a-4803-9686-9a7a7374c74d)

Therefore, I would use IDAPro 32-bits to see the full source code of this file. And here is `main()` and `vuln()`:

![mainFunc](https://github.com/OceanTran999/BDSEC2023/assets/100577019/31850714-7384-4a98-a029-91c210ccce13)

![vulnFunc](https://github.com/OceanTran999/BDSEC2023/assets/100577019/cdefe217-0db9-4b22-a2b0-62272f77d8bf)

Then I checked the protection of this file. As the result, the file had no protection.

![checksec](https://github.com/OceanTran999/BDSEC2023/assets/100577019/f3f81cd3-6185-4843-91f5-b684a66c5845)

Next, we will `disassemble vuln`:

I suddenly saw `mov  DWORD PTR [ebp - 0xc], 0x123456678`. Therefore I considered that the address of variable "v1" will be `ebp-0xc`

![v1](https://github.com/OceanTran999/BDSEC2023/assets/100577019/3b4b83ff-da06-4a50-b7db-fe453cb1dd2c)

Next, before call the `gets()` function, I saw there was a code: `lea  eax, [ebp-0x2c]`. Therefore I thought the address of gets() function will be `ebp-0x2c`

![gets](https://github.com/OceanTran999/BDSEC2023/assets/100577019/b6a7e684-951f-40a6-84d3-341225286b74)

After that, I saw the address `ebp-0xc` compare with the value `0xdeadbeef`. So, I realized that I had to overwrite the v1 value to get the flag.

![deadbeef](https://github.com/OceanTran999/BDSEC2023/assets/100577019/92f566b8-740b-42dc-8f10-79794802cac8)

Here is my stack that I drew it.

![stack](https://github.com/OceanTran999/BDSEC2023/assets/100577019/b3fe8d09-288a-4294-9d00-dd021c701db2)

Wakuwaku~~ I finally got the flag

![Flag](https://github.com/OceanTran999/BDSEC2023/assets/100577019/24e27b84-5fc5-428c-979d-ce37573b3a90)

_**Sadly :( these 2 beneath challenges I didn't have time to solve, but I was able to solve it after the competition XD**_

# callme
Type of file:

![readelf](https://github.com/OceanTran999/BDSEC2023/assets/100577019/14100d70-606b-4331-ae17-f14e0dc80ef1)

Used IDAPro 32-bits, I got source code. Here's the `main()` function

![mainFunc](https://github.com/OceanTran999/BDSEC2023/assets/100577019/29dc3b4e-8dda-4b1e-aa8b-2fff2a1f5315)

![mainFunc_2](https://github.com/OceanTran999/BDSEC2023/assets/100577019/ac73c539-6663-4f6a-bce5-bf000248f979)

Check the file's protection:

![checksec](https://github.com/OceanTran999/BDSEC2023/assets/100577019/17145c7f-74be-4cf7-b857-c82d3f757cbd)

Then I `disassemble main`. And did as same as the _**AnyaForger**_ challenge

![scanf](https://github.com/OceanTran999/BDSEC2023/assets/100577019/a1a971a5-f7cd-4e32-bf75-4c6d16575eff)

![test](https://github.com/OceanTran999/BDSEC2023/assets/100577019/28534e8a-e256-4c2e-bd83-ebf53d9355b5)

Finally, I got stack like this:

![stack](https://github.com/OceanTran999/BDSEC2023/assets/100577019/a4bd7ee6-2f51-41e3-96f7-49dd9b2d777e)
28)

Booom!!!! I got the flag. EZPZ

![flag](https://github.com/OceanTran999/BDSEC2023/assets/100577019/613dc8b6-1cb0-4654-b3b6-425f2e57ce61)


# ghost
Here we got the protections

![checksec](https://github.com/OceanTran999/BDSEC2023/assets/100577019/95a55e00-77cb-4ffc-93b0-ff124bff389c)

Then I check the type of file and it is the ELF 64-bits

![readelf](https://github.com/OceanTran999/BDSEC2023/assets/100577019/caae748c-65d1-4013-b630-e4f446faaeab)

Therefore, I had to use IDAPro 64-bits to observe the source code. Here's the `main()` function:

![SourceCode](https://github.com/OceanTran999/BDSEC2023/assets/100577019/dd192010-f14a-41b7-b718-aa4505717fd8)

Did as same as those 2 above challenges. I got the stack like this:

![stack](https://github.com/OceanTran999/BDSEC2023/assets/100577019/5062f22a-2f55-4ed2-a6cb-b410f8c5e760)

Finally, submit to server and I got the flag. Yayyyyy :D

![Flag](https://github.com/OceanTran999/BDSEC2023/assets/100577019/2092c5d6-660f-40ec-8a7c-7990fa790604)
