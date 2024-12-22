# anyaForger
First, let's see type of file, I saw this is ELF32 file.

![readelf](https://github.com/user-attachments/assets/336a2ee3-efa4-497b-a222-65cbcc6ed7a2)


Therefore, I would use IDAPro 32-bits to see the full source code of this file. And here is `main()` and `vuln()`:

![mainFunc](https://github.com/user-attachments/assets/b27fc834-3d34-4cb7-9094-52f18149c4fa)

![vulnFunc](https://github.com/user-attachments/assets/d79bd065-c5da-4334-87ff-9139f8afc86d)

Then I checked the protection of this file. As the result, the file had no protection.

![checksec](https://github.com/user-attachments/assets/409710c4-6efe-47eb-bf53-41046fa58950)

Next, we will `disassemble vuln`:
![disassem_vuln](https://github.com/user-attachments/assets/f427b591-8ae3-4029-98bf-0fc1e2a787d0)


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

![readelf](https://github.com/user-attachments/assets/ff813451-c6b1-4b2a-bb58-12b7b6896759)

Used IDAPro 32-bits, I got source code. Here's the `main()` function

![mainFunc](https://github.com/user-attachments/assets/2747d934-e0ad-4e2e-842b-057858015614)

![mainFunc_2](https://github.com/user-attachments/assets/f8f9acaa-c3b2-48a8-86e3-fedfc7601bf0)

Check the file's protection:

![checksec](https://github.com/user-attachments/assets/ed1a0053-c701-42b4-802f-bfc6fc9a3fa0)

Then I `disassemble main`. And did as same as the _**AnyaForger**_ challenge
![diassem_main](https://github.com/user-attachments/assets/2e8ad733-3591-47ba-97cf-6565c187ea7c)


![scanf](https://github.com/user-attachments/assets/74792e59-5682-4847-8b80-dff9d2a74496)


![test](https://github.com/user-attachments/assets/84968c5b-d7d5-45ee-a1ce-5cbefac26682)


Finally, I got stack like this:

![stack](https://github.com/user-attachments/assets/9da01994-5e44-41ba-a110-635d51fd6937)

Booom!!!! I got the flag. EZPZ

![flag](https://github.com/user-attachments/assets/4554278c-7d0b-4b25-8dab-aa3a3d73b510)


# ghost
Here we got the protections

![checksec](https://github.com/user-attachments/assets/12028f2a-9032-45b5-ab5e-f9db4aeca292)

Then I check the type of file and it is the ELF 64-bits

![readelf](https://github.com/user-attachments/assets/8c3e52c3-2028-43d7-83b5-c34c09e2a5c3)

Therefore, I had to use IDAPro 64-bits to observe the source code. Here's the `main()` function:

![SourceCode](https://github.com/user-attachments/assets/d1a497e4-4a90-4675-bb92-92bb6fb29b21)

Did as same as those 2 above challenges. I got the stack like this:

![stack](https://github.com/user-attachments/assets/abd59cb6-558b-4e17-b5e6-b9bb3b24d9ec)

Finally, submit to server and I got the flag. Yayyyyy :D

![Flag](https://github.com/user-attachments/assets/d8dd3efd-8290-4043-ad3e-cc66ba8dbf9c)
