**I solved this challenge after the competition 😢**
![chall](https://github.com/user-attachments/assets/e8e4f369-f8a9-47ad-b405-fa4bad856610)


At first, I thought I have to win the game to get the flag. But it's so hard to win it :(. So I read the hint and they say that I have to read the code and understand the Websocket.

After reading the page source, I realize that there are some functions that can help us to interact with the WebSocket, which is defined in `/ws/`.

![ws](https://github.com/user-attachments/assets/05d27b92-02e5-477a-9645-97c26a1b4b7c)


We can see that we can interact with the server with `mate <random number>` or `eval <random number>`. I test with `mate 0` first, we can see that the fish's response seems to be different.

![eval_matte](https://github.com/user-attachments/assets/90884d79-796a-4af3-920e-cc684633610a)


![mate0](https://github.com/user-attachments/assets/73b3ce89-4324-441f-9642-9d294546b2e1)


However, if I give the `n` value, the server will response with my `n` value. I also test with the negative number, but their response are same as `0` value. So I decide to change to `eval`.

![maten](https://github.com/user-attachments/assets/f47e76f3-6368-4b93-98d0-84b2c36ba04a)


![matenegN](https://github.com/user-attachments/assets/23681262-ce3b-45b8-b548-f3aae1d9e117)


![eval0](https://github.com/user-attachments/assets/3782ce42-3c13-4682-a4b2-18f5fc2124e2)


When testing with value `1000`, I saw the difference.

![eval1000](https://github.com/user-attachments/assets/1a21a709-6b66-4974-89dd-a0e5233576c9)


But after testing the bigger values, I see there's no difference from the response. So I think I should provide the negative number and get the flag XD.

![flag](https://github.com/user-attachments/assets/793b77e2-3fd7-4a24-bcf3-dd7a81cacbb1)
