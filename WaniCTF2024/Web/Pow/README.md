**I didn't solve this challenge during the competition, after asking for some good players after CTF, I decide to solve it again.**

![Chal](https://github.com/user-attachments/assets/1b1e0f43-aabf-4220-b3d9-f33325334fd0)


At first I thought I have to calculate the hash in `.js` files to get the flag LOL :) .

![Burp2](https://github.com/user-attachments/assets/d8beb40c-6db6-40e9-bcef-0f06472e0758)


Using `Burp Suite`, we can see that the HTTP request has `pow_session=eyJhbGc....` in `Cookie` and an array which has `["52592778"]`, you can take another values when the server sends you.

![Burp3](https://github.com/user-attachments/assets/97e8150b-aaf8-48bc-8bc7-4ce58dd77762)


And when you receive the request, the value of **Server response** will be `progress: 1/1000000`.

![Check_Burp3](https://github.com/user-attachments/assets/3f70133d-fc1d-4495-9bce-a2769a04f83e)


Therefore, whatif we increase the number of elements, what will happen?

![Burp4](https://github.com/user-attachments/assets/1791656f-3033-4e98-84ef-e4fe63f75192)


The answer is the value will be **increase** too when we send to server.

![Checck_Burp4](https://github.com/user-attachments/assets/e061250d-1a34-40a5-a3a1-e167f61fb1b6)


So I will write Python script and send to the server with an array has `1000000` elements.

![Error](https://github.com/user-attachments/assets/6b358608-ba9b-40f5-8802-f5835908a7f8)


And it seems that the server they limit the number of elements in an array, therefore we have to decrease them. After trying, the `10000` elements will be suitable to exploit. Finally, you just need to run the script several times until you get the flag.

![Flag](https://github.com/user-attachments/assets/9da4d520-a12b-4977-9454-e22b4e8aa7b6)
