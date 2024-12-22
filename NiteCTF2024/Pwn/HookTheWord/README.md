![Chal](https://github.com/user-attachments/assets/7a540d54-2075-46ee-a5e9-1514ddbc6937)

# My solution
First, checking the protection and I see that it seems it has full protection.
![checksec](https://github.com/user-attachments/assets/1429cb29-2bcc-4d59-841c-991eda7cab01)


When seeing the `hook` in the name of challenge, it reminds me about the overwriting `__malloc_hook()` or `__free_hook()` attack, so checking the `libc.so.6` file and it has it. The program has the `Use After Free(UAF)` or `Double Free` vulnerability, but..., how to get the address of these function because the program has `PIE` which the address of binary changes everytime it runs...
![strings](https://github.com/user-attachments/assets/65f4230c-5515-462e-8d3d-19f08312c524)


# Final solution
Firstly, to make the local exploit same as remote exploit, I just know that the `pwninit` tool can do that.
So asking in the discord with my nubbie question, I understand that we have to use `malloc_consolidate()`, which we will overwrite the list of `tcache_bins`, which has only 7 elements with size of chunks **more than 0x90** and `malloc()` again to make unsorted bin.
![discord_help](https://github.com/user-attachments/assets/01008f47-580b-443c-8c50-baf6090c9a27)


So yeah, after doing that and use `pwndbg`, I see that it leaks the address in the `libc`, calculate the offset we will have the address of libc base.

![vmmap](https://github.com/user-attachments/assets/b3a16107-2110-4232-9de7-37d4cabe4cba)


Great!!! Things seem to be easier, now let's just find the address of those `hook()` function and use `Double Free` attack to exploit.

![readelf](https://github.com/user-attachments/assets/fb04b607-a5f9-4458-934d-3d5e82c56796)


![pwndbg_overwritecheck](https://github.com/user-attachments/assets/42819527-5621-43b4-aa49-e951337ad912)


We really overwrote the `chunk->next`, so when we `malloc()`, it will point to the address that has `free_hook()`, and we will use the `fill_chunk()` function to change it to another address such as `system()`. In local, I see that it is pointing to the address that doesn't have `WRITE` permission, so I will add more offset so that it points to `__free_hook()` directly.

![shell_local](https://github.com/user-attachments/assets/41ed5bda-c8dc-4a2f-8b5f-79995a2e9d09)
