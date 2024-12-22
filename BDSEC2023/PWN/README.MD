# anyaForger
First, let's see type of file, I saw this is ELF32 file.

![readelf](https://github.com/user-attachments/assets/336a2ee3-efa4-497b-a222-65cbcc6ed7a2)


![disassem_vuln](https://github.com/user-attachments/assets/f427b591-8ae3-4029-98bf-0fc1e2a787d0)


Therefore, I would use IDAPro 32-bits to see the full source code of this file. And here is `main()` and `vuln()`:

![mainFunc](https://github.com/user-attachments/assets/b27fc834-3d34-4cb7-9094-52f18149c4fa)

![vulnFunc](https://github.com/user-attachments/assets/d79bd065-c5da-4334-87ff-9139f8afc86d)

Then I checked the protection of this file. As the result, the file had no protection.

![checksec](https://github.com/user-attachments/assets/409710c4-6efe-47eb-bf53-41046fa58950)

Next, we will `disassemble vuln`:

I suddenly saw `mov  DWORD PTR [ebp - 0xc], 0x123456678`. Therefore I considered that the address of variable "v1" will be `ebp-0xc`

![v1](https://github.com/user-attachments/assets/f4138174-1647-4ad3-8bb4-0b3b012d253b)

Next, before call the `gets()` function, I saw there was a code: `lea  eax, [ebp-0x2c]`. Therefore I thought the address of gets() function will be `ebp-0x2c`

![gets](https://github.com/user-attachments/assets/4a9ff0de-a037-4eb8-b2f8-0413b7cf3030)

After that, I saw the address `ebp-0xc` compare with the value `0xdeadbeef`. So, I realized that I had to overwrite the v1 value to get the flag.

![deadbeef](https://github.com/user-attachments/assets/bcf58841-b3ea-4505-877d-7ec43d4a43f7)

Here is my stack that I drew it.

![stack](https://github.com/user-attachments/assets/9b9eafe2-670f-4c9d-bb0f-d69fa46f7dbb)

Wakuwaku~~ I finally got the flag

![Flag](https://github.com/user-attachments/assets/c6c2212f-148b-4a9f-ab07-6645cc041daf)

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
