![chal](https://github.com/user-attachments/assets/30b6b1c3-c5c3-499d-bb10-d683c79c2483)


![access](https://github.com/user-attachments/assets/c0eceede-2bdf-4e5b-9d2c-893a1eb49fde)


The challenge is giving a web that will display the user's input.

![output](https://github.com/user-attachments/assets/8e14510b-2e77-43e7-8434-1a493a939b2e)


At first I try to inject a Javascript code to the input.

![inject_js](https://github.com/user-attachments/assets/aeb62923-012a-43ed-a591-3e99ca1ba4ec)


![output2](https://github.com/user-attachments/assets/1cab579c-7bdf-4bb3-87aa-fc9c809aa639)


So, the web server really has a vulnerability. I try to inject the Javascript to the template server to check whether the side of server responses my malicious input. And yes, it is really using the `Jinja2` template.

![Server_side](https://github.com/user-attachments/assets/e0724156-62d2-43df-9302-8b794f249dd5)


![jinja2_detection](https://github.com/user-attachments/assets/cdd619e5-8680-4978-881a-bcc98ddf8496)


Finally, I just need to use the payload from HackTricks to get the RCE :)

![rce](https://github.com/user-attachments/assets/dcac6737-13b7-4a84-bc9a-0ad6b2b1276c)


![flag](https://github.com/user-attachments/assets/88e16355-2049-49b5-bd03-19a5bd8e3b7d)
