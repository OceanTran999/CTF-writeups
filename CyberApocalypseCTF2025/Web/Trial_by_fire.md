The challenge provide me the full source code of the web server, so let's take a look a bit. We see that there's a variable called `warrior_name`.

![code1](https://github.com/user-attachments/assets/f5b6ff74-b7f5-4076-9eae-0545858275de)


In the `routes.py` file in the `blueprints` folder, I saw that the web developer use `warrior_name` variable to display the user's input when the game is over and the result board appears. This allows attackers to inject a malicious code to a template to create a RCE.

![code2](https://github.com/user-attachments/assets/006dd9b5-fcd5-4d49-951c-18486bed8a89)


First, I will try to inject a Javascript code to display a notification.

![XSS_out](https://github.com/user-attachments/assets/82972378-a055-47a3-a920-95cb569bc6ae)


In the `app.py` file, I see the programmers use `Flask` library, which means website is used with `Jinja2` template.

![flask_detection](https://github.com/user-attachments/assets/1c1ccc25-dc73-4e1a-a844-832ff526fd1a)


So, I will try to test the Server-side Template Injection (SSTI) first to see whether this exploit could be worked.

![test_SSTI](https://github.com/user-attachments/assets/62421cda-dec4-4551-b49a-56833e898107)


![output_SSTI](https://github.com/user-attachments/assets/cce079d8-66ac-4919-b987-a4fb320fcb30)


However, we can't test directly in the web's input because it limits the length, so we will test it in Burp.

![burp_test](https://github.com/user-attachments/assets/ba0f94b7-6b85-4c80-94df-e932a91a358b)

![burp_output](https://github.com/user-attachments/assets/aa07b9c6-b7dd-4918-a3f0-ddadd85b52f2)


Finally, we get the flag.

![flag](https://github.com/user-attachments/assets/a7c33bcf-5b55-40db-887b-59030da5bfd4)
