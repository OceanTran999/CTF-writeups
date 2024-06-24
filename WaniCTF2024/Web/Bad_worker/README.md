![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/63a065ff-fa38-412d-9bf1-45df72c01678)


While scanning all the target website, I see the `Fetch data` tab will display the flag for us.

![Fetch_data](https://github.com/OceanTran999/CTF-writeups/assets/100577019/6d062192-75d9-4702-ab87-f7c2987c8bf5)


But it seems it gives us the fake flag....

![Dummy](https://github.com/OceanTran999/CTF-writeups/assets/100577019/7ac0fa00-e76a-4846-baaa-841bccb8b80f)


Using `Burp Suite`, I see that they give us the `DUMMY.txt`, but we need the `FLAG.txt` file to get the real flag.

![Burp](https://github.com/OceanTran999/CTF-writeups/assets/100577019/26903a54-2164-45f4-9453-8a30b6286b34)


 I just need to turn on the `Intercept`, replace `DUMMY.txt` to `FLAG.txt` and send the HTTP Request packet to the server. And we will get the real flag.
 
![Flag](https://github.com/OceanTran999/CTF-writeups/assets/100577019/9844e2bb-7c1b-4155-8012-5289b45c3146)
