At first, I thought I have to win the game to get the flag. But it's so hard to win it :(. So I read the hint and they say that I have to read the code and understand the Websocket.

After reading the page source, I realize that there are some functions that can help us to interact with the WebSocket, which is defined in `/ws/`.




We can see that we can interact with the server with `mate <random number>` or `eval <random number>`. I test with `mate` first, we can see that the fish's response seems to be different.


However, if I give the `n` value, the server will response with my `n` value. So I decide to change to `eval`.



When testing with value `1000`, I saw the difference.



But after testing the bigger values, I see there's no difference from the response. So I think I should provide the negative number and get the flag XD.

