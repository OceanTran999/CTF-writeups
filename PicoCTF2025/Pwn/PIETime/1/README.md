![Chal](https://github.com/user-attachments/assets/7adef992-97e9-4356-925c-6a2f3695491a)


![checksec](https://github.com/user-attachments/assets/7c03bca8-c8ab-4f5a-89d2-cf867a5e2ab6)


The challenge gives us the value of `main()`'s address, the binary also has the PIE protection which the address values change everytime we run the program. However, the distance is still the same, so we just calculate the `win()` address from the given `main()` to get the flag.

![pwndbg](https://github.com/user-attachments/assets/2387ddbb-c4d3-461e-a702-877aafed21fb)


![flag](https://github.com/user-attachments/assets/eb11d0e1-f5d1-4d54-8a90-4e5549eb95c2)
