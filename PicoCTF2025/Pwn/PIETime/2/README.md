![Chal](https://github.com/user-attachments/assets/e06c4825-81a3-4ada-8ace-a70ee129b8e7)


![code](https://github.com/user-attachments/assets/a3d1b39b-f6d7-43d2-b98c-3ee904d92284)


Looking at the line 15, we see that there's a format string vulnerability, so the first input we need to leak the `main()` address that has `0x00` in the lowest byte. After leaking the `main()` address, we just calculate the `win()` address and get the flag.

![run](https://github.com/user-attachments/assets/043536e3-fa28-4dc8-92f0-4e51901b6b0e)


![flag](https://github.com/user-attachments/assets/eae58150-1768-4efb-8927-def9abde3f6e)
