# IP Addr
![Chal](https://github.com/OceanTran999/BDSEC2023/assets/100577019/7ca8a227-a11c-4074-94e3-798bd09ec237)

First, I think most people will `ping` to the Server, so I decided to search ICMP Protocol

![icmp](https://github.com/OceanTran999/BDSEC2023/assets/100577019/5585ef18-e61c-423d-9398-093d65aa6ec2)

As you can see, there are "ICMP request" and "ICMP response" packets which you'll know the flag.

Flag: ```BDSEC{192.168.1.5_192.168.1.7}```

# Hostname
![Chal](https://github.com/OceanTran999/BDSEC2023/assets/100577019/566bc835-a7be-4834-9aad-18b4a73f13a8)

To find hostname, I used filter with ```http.host```

![Hostname](https://github.com/OceanTran999/BDSEC2023/assets/100577019/5bd8af52-3774-4b5c-b5d4-334b31214c7c)

Flag: ```BDSEC{nanomate-solutions.com}```

# Follow the Path
![Chal](https://github.com/OceanTran999/BDSEC2023/assets/100577019/bd11b4b8-06ee-44dd-bccb-0348ea92b456)

In this challenge, I also used HTTP packets to find the path.

![http](https://github.com/OceanTran999/BDSEC2023/assets/100577019/1af22786-3d6a-40ef-9197-d75752daad86)

Flag: ```BDSEC{/app/admin_panel}```

# Compromised Account
![Chal](https://github.com/OceanTran999/BDSEC2023/assets/100577019/cd4473ff-0ca4-4986-a666-69d063f2db2a)

Sadly, I couldn't solve this challenge so I decided to solve it after the competition.
At first, I thought this was an easy challenge. But nahhh, I was faked by this account.

![fake_ans](https://github.com/OceanTran999/BDSEC2023/assets/100577019/da9fe17e-3eff-431e-b9ec-6071ae0c7d4c)

I asked in Discord and luckily, a good member helped me.

![discord_help](https://github.com/OceanTran999/BDSEC2023/assets/100577019/d47da44f-65b7-443a-a6e6-8703fb48df84)

Therefore, I tried to find the packet which had "Login successful"

![find_packet](https://github.com/OceanTran999/BDSEC2023/assets/100577019/88dedf3c-9977-4d48-b8dc-5e5e765698de)

Flag: ```BDSEC{tareq@gmail.com_tareq@nanomate}```
