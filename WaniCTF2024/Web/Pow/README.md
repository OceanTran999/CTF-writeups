**I didn't solve this challenge during the competition, after asking for some good players after CTF, I decide to solve it again.**

![Chal](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/eb0608af-8f31-49cb-9387-180d5d809557)


At first I thought I have to calculate the hash in `.js` files to get the flag LOL :) .

![Burp2](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/6796f6eb-59b6-44b2-a213-456b2dbea866)


Using `Burp Suite`, we can see that the HTTP request has `pow_session=eyJhbGc....` in `Cookie` and an array which has `["52592778"]`, you can take another values when the server sends you.

![Burp3](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/1dfe53d6-5b53-4f15-b0d2-6602d0a8a58d)


And when you receive the request, the value of **Server response** will be `progress: 1/1000000`.

![Check_Burp3](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/c8c242e6-c0fc-4498-b32d-38bbf6acbd37)


Therefore, whatif we increase the number of elements, what will happen?

![Burp4](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/8df042b3-e540-43b1-86c6-27d789f6c0d1)


The answer is the value will be **increase** too when we send to server.

![Checck_Burp4](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/9e77c91d-cb96-4936-a493-02072d992d67)


So I will write Python script and send to the server with an array has `1000000` elements.

![Error](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/ab3a93a8-01dd-4952-bffd-26226b61677f)


And it seems that the server they limit the number of elements in an array, therefore we have to decrease them. After trying, the `10000` elements will be suitable to exploit. Finally, you just need to run the script several times until you get the flag.

![Flag](https://github.com/OceanTran999/WaniCTF2024/assets/100577019/4f67b2c9-4e36-4b2f-9c72-cb30fa314dda)
