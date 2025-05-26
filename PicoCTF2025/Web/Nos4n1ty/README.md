![chal](https://github.com/user-attachments/assets/759130c6-dc45-4a34-8143-fe08449e4e30)


![access](https://github.com/user-attachments/assets/a1e9e8ae-3466-4f33-bd40-8f71b1a7ea79)


The challenge gives us an upload file web, so I will try whether we can upload the shellcode file to the web server and get the shell. First, I create a simple file `.php` to run the `id` shell command, and upload to the web server.

![leak_path](https://github.com/user-attachments/assets/9cff973c-9c9c-4766-9683-aa42d8447bfe)


I can see it leaks the path of the uploaded file, so let's navigate to it.

![rce](https://github.com/user-attachments/assets/9d6f9f4d-1314-4a96-8a56-fd6aa9e8139e)


Perfect, now we will upload the web shell to the web server to get the flag.

![flag](https://github.com/user-attachments/assets/060774f4-2ccd-448c-aace-20959510c17a)
