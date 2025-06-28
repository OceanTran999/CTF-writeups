** I did not solve during the competition due to lack of time :(**

The challenge provides an calculator application that users can provide a mathematic query to know the answer. After testing some inputs, I see that the app runs in Python. However, viewing the source page, I see that they filtered some malicious keywords to prevent from RCE. Also, some keywords like `\`, and `/` also are blocked.



Therefore, I have 2 solution in this challenge, first is using `open().read()` to read the `/flag.txt`, because they block `/` so I will use `chr('/')` to bypass this :).


The second one is because I want to learn more about the `subprocess` module. After searching in Google, I see that the `subprocess` module is used to call new process by Python. Therefore, to display the content of `/flag.txt`, I will use `subprocess.check_output(["cat","/flag.txt"])`. But the filter will block the `cat`, so whatif I use this `'c'+'a'+'t'`.



And we got the flag XD