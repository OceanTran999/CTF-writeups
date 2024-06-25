# IP Addr
![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/e0380325-db13-4b04-9a93-180c9cb676a6)

First, I think most people will `ping` to the Server, so I decided to search ICMP Protocol

![icmp](https://github.com/OceanTran999/CTF-writeups/assets/100577019/b9e4752a-4f60-45c0-afa2-ca3a13aca6a5)

As you can see, there are "ICMP request" and "ICMP response" packets which you'll know the flag.

Flag: ```BDSEC{192.168.1.5_192.168.1.7}```

# Hostname
![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/a9c6d246-1dbb-4e47-8e24-9dea2d24b93d)

To find hostname, I used filter with ```http.host```

![Hostname](https://github.com/OceanTran999/CTF-writeups/assets/100577019/60158826-0e31-4a78-94d2-1dbc4462d9b0)

Flag: ```BDSEC{nanomate-solutions.com}```

# Follow the Path
![Chal](https://github.com/OceanTran999/CTF-writeups/assets/100577019/42debc35-66ea-4759-a2ff-f4f7f79d1cff)

In this challenge, I also used HTTP packets to find the path.

![http](https://github.com/OceanTran999/CTF-writeups/assets/100577019/21984852-3cb7-4ad4-87c0-a32595111eef)

Flag: ```BDSEC{/app/admin_panel}```

# Compromised Account
![Chal](https://github.com/OceanTran999/CTF-write![Uploading fake_ans.png…]()

Sadly, I couldn't solve this challenge so I decided to solve it after the competition.
At first, I thought this was an easy challenge. But nahhh, I was faked by this account.

![fake_ans](https://github.com/OceanTran999/CTF-writeups/assets/100577019/4f7c16d9-5395-4858-9814-bc1a3099df04)

I asked in Discord and luckily, a good member helped me.

![discord_help](https://github.com/OceanTran999/CTF-writeups/assets/100577019/14ba9a81-a3c2-48d8-985a-db67ff367386)

Therefore, I tried to find the packet which had "Login successful"

![find_packet](https://github.com/OceanTran999/CTF-writeups/assets/100577019/36c3839d-e4f8-4048-bf94-2295f2e1de34)

Flag: ```BDSEC{tareq@gmail.com_tareq@nanomate}```
