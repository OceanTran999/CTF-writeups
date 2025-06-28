**I did not solve during the competition due to lack of time :(**

![chall](https://github.com/user-attachments/assets/71648089-1dd6-4015-b11b-7ec5942bd0a0)


The challenge provides an calculator application that users can provide a mathematic query to know the answer. After testing some inputs, I see that the app runs in Python. However, viewing the source page, I see that they filtered some malicious keywords to prevent from RCE. Also, some keywords like `\`, and `/` also are blocked.

![page_source](https://github.com/user-attachments/assets/8f4b8fbe-2827-452e-ad16-b0498da3c1e4)


Therefore, I have 2 solution in this challenge. There is another solution is that I try to find the `subprocess.Popen()` by solving same as the `ssti` challenges, but I am still be blocked by the filter... My first solution is using `open().read()` to read the `/flag.txt`, because they block `/` so I will use `chr('/')` to bypass this :).

![sol1](https://github.com/user-attachments/assets/884008ce-5560-43e9-9244-e2a52004e390)


The second one is because I want to learn more about the `subprocess` module. After searching in Google, I see that the `subprocess` module is used to call new process by Python. Therefore, to display the content of `/flag.txt`, I will use `subprocess.check_output(["cat","/flag.txt"])`. But the filter will block the `cat`, so whatif I use this `'c'+'a'+'t'`.

![sol2](https://github.com/user-attachments/assets/ff52d794-1f5a-492a-8b60-1cfef652c209)


And we got the flag XD
