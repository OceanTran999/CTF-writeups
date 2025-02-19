![checksec](https://github.com/user-attachments/assets/fa862ed4-5ed6-42b5-b316-30fcdac1fd65)


This challenge I couldn't solve during the competition because I didn't use the `patchelf` tool in the right way :)
So to change the path of dynammic library, the commands will be:
```
  patchelf --set-interpreter [ld file] [target binary]
  patchelf --replace-needed [default libc file] [libc file that want to change] [target binary]
```

First I found that the program have the heap overflow bug, but the program will soone be cracked if I create a new chunk in the next step...

![heap_over1](https://github.com/user-attachments/assets/567473d2-90f2-4d90-86f6-ae0029b26052)


![heap_over2](https://github.com/user-attachments/assets/88b46767-8d1a-4c57-8864-5b2bf245a987)


So after using `patchelf` successfully, the version of library that target server using is `GLIBC2.31`, which has some `hook()` function. First I will leak the libc address by triggering `malloc_consolidate()`, next I will calculate the offset of `free_hook()` and modify its address with `system()` using UAF vulnerability. Finally create a new chunk with a content `/bin/sh` and free it, we will get the shell ;)

![libc_leak](https://github.com/user-attachments/assets/dcc4a386-1b2e-4b5d-b283-588797c6064d)


![hookfuncs](https://github.com/user-attachments/assets/21be30d2-11c2-440e-8494-801ec4dcee6b)


![flag](https://github.com/user-attachments/assets/6d45226d-51f3-4ce2-b4fa-917b8c260467)
