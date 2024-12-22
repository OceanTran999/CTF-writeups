# IP Addr
![Chal](https://github.com/user-attachments/assets/b05bbd3f-f29d-45b9-889b-24c66b36f067)

First, I think most people will `ping` to the Server, so I decided to search ICMP Protocol

![icmp](https://github.com/user-attachments/assets/f684627f-13c1-441a-8c0d-355fae6176bf)

As you can see, there are "ICMP request" and "ICMP response" packets which you'll know the flag.

Flag: ```BDSEC{192.168.1.5_192.168.1.7}```

# Hostname
![Chal](https://github.com/user-attachments/assets/a3a01670-93f8-4159-907e-fb48d5360bfb)

To find hostname, I used filter with ```http.host```

![Hostname](https://github.com/user-attachments/assets/4db5553b-39b4-4609-878b-f83e6275d240)

Flag: ```BDSEC{nanomate-solutions.com}```

# Follow the Path
![Chal](https://github.com/user-attachments/assets/9c10374f-a131-4ece-bc91-78183353dabc)

In this challenge, I also used HTTP packets to find the path.

![http](https://github.com/user-attachments/assets/23b9d461-d3cc-449b-b442-8feb92f0a8c1)


Flag: ```BDSEC{/app/admin_panel}```

# Compromised Account
![Chal](https://github.com/user-attachments/assets/c7795a5f-50c0-4d4c-bf69-06b2c7f8bc64)

Sadly, I couldn't solve this challenge so I decided to solve it after the competition.
At first, I thought this was an easy challenge. But nahhh, I was faked by this account.

![fake_ans](https://github.com/user-attachments/assets/9f089c2f-b74d-4b36-a5aa-acb5c25ed8ce)

I asked in Discord and luckily, a good member helped me.

![discord_help](https://github.com/user-attachments/assets/647e7e94-cc0d-457b-9099-9fb8c103270e)

Therefore, I tried to find the packet which had "Login successful"

![find_packet](https://github.com/user-attachments/assets/4ee2e2e5-cc03-4fe1-bc6d-a4c1a33a6a42)

Flag: ```BDSEC{tareq@gmail.com_tareq@nanomate}```
