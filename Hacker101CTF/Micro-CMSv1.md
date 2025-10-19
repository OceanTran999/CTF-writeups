The challenge gives a website to create a webpage using Markdown

<img width="624" height="154" alt="web" src="https://github.com/user-attachments/assets/9bcb7b93-3e7d-48d5-a78a-e673609111e6" />


First, checking the source code of webpage, I see that there are 2 pages defined with `page/<number_of_page>`, so I think about directing to other URL to see if there is any useful information or the best thing is... the flag.

<img width="624" height="286" alt="web_source" src="https://github.com/user-attachments/assets/204c9682-1801-4fae-91bc-8649044a15c9" />


After bruteforcing from 3 to 10, I see that in `page 7`, there is a `Forbidden` response.

<img width="624" height="127" alt="forbidden_page" src="https://github.com/user-attachments/assets/40fc2ea4-ec2d-42da-8ff9-1e8a0e10256a" />


Therefore, I think this page must be the target. So how to bypass it? The website allows us to edit our Markdown test. So what if we change our current URL and direct to the index of the target webpage we want to?

<img width="624" height="369" alt="ex_editpage" src="https://github.com/user-attachments/assets/41d4fa86-248e-44ac-a882-9c89293db143" />


And here's our first flag XD.

<img width="624" height="361" alt="flag1" src="https://github.com/user-attachments/assets/f1dfe918-ee50-476f-87ff-39fdab78fef1" />


Next, I try to create my own Markdown website.

<img width="624" height="355" alt="createpage" src="https://github.com/user-attachments/assets/3aaa8511-4b69-4ebc-a75b-0c7f0eafa587" />


Looking at the content box, I know this must be the `XSS attack`. I try to test the input with alphabetic, numberic and special character `<`, `>`.

<img width="624" height="248" alt="source_createpage" src="https://github.com/user-attachments/assets/d65af315-48b2-489c-b917-e420318be1d0" />


However, the result does not allow us to input with special character to execute the Javascript with `<script>` tag. So what if, we can try to other HTML tag? Such as `<img>`, because the Markdown also allows this tag, right?

<img width="624" height="199" alt="img_tag" src="https://github.com/user-attachments/assets/2f7167b1-c2eb-466d-95c3-b5f50944bc2c" />


And problem solved, our attack is executed successfully.

<img width="624" height="258" alt="img_tag_sc" src="https://github.com/user-attachments/assets/388092ef-4a9c-4f6e-8459-81b92e198483" />


<img width="624" height="118" alt="xss__ok" src="https://github.com/user-attachments/assets/1e245f8f-1b6f-41ff-98b1-f36e2c9d3986" />


I think there must be a box in this challenge, but when seeing this is an easy challenge, I think I don't have to do this part, so after finding, I see the flag in the source code. XD

<img width="624" height="172" alt="flag2" src="https://github.com/user-attachments/assets/a29de425-ae24-4d39-adbf-e7dce9473a57" />


And don't know why when I redirect to the Home page, I also get the flag XD. Double flag in 1 exploit.

<img width="624" height="111" alt="flag3" src="https://github.com/user-attachments/assets/7a2fcca4-d7a4-4167-81d2-87ed03447f33" />
