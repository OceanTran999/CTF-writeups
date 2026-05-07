# Writeup
This challenge is very hard for me, despite of reading the HINT, I still can't understand :) .

So reading the writeup of the challenge, here's the payload to exploit:

```
<form><math><mtext></form><form><malignmark><style></math><img src onerror=alert(1)>
```

## Testing input and analyzing code
First, I try to inject with `<h2>Siuuu</h2>` and my input was work, also when I don't add `</h2>` my input is still work because of the `Document Fragment`. I also tried with some of my inputs such as `<p><h1>Siuuu`, reading the `Console`, the output to inject into `<template>` is `<p></p><h1>Siuuu</h1>`. Next step, I will analyze the XSS sanitization code:
- First, our input will be added to `<template>` tag.
- Next, the `<template>` content will passed into the first element of `nodes` array, and do a loop to check if the length of `node` is larger than `0`
    - During the loop, first it take the **final element** from the `nodes` to pass to `n`.
    - Then it will check the attributes of `n` to remove them, which we can't use `<img src onerrors=alert(1)>` directly.
    - Then checking if the current element is kind of `<script>` tag to remove it.
    - Finally, if the current element passes all the condition of sanitization, it will add at the end of `nodes` array.

## Payload, MathML's tags and explain
Ok, so what exactly the payload of the writeup works? According to blogs I mention in the References, but first let's talk some tags in the payload:
- `<math>` is **MathML (Mathematics Markup Language)** for displaying mathematics webpages.
- `<mtext>` is to render arbitrary text with no notational meaning, such as comments or annotations. For displaying `identifier`, `numeric` or `operator` elements we can use `mi`, `mn` and `mo` tag respectively.
- [<malignmark>](https://www.data2type.de/en/xml-xslt-xslfo/math-ml/presentation-elements/malignmark) is to indicate an alignment point inside an alignment group in a table column.
- [<mglyph>](https://www.data2type.de/en/xml-xslt-xslfo/math-ml/presentation-elements/mglyph) is to allow arbitrary symbols and other extended characters to be displayed. It is displayed as a specific glyph in a specific font, the values of which are determined by its attributes, this tag can't be used due to the last check of sanitization.

The `<style>` mostly is considered as a magical tag that make our payload harmless and not being removed because I understand that the browser will interpret our payload as comment (correct me if I'm wrong XD). When sending the writeup's payload to the server, the browser will automatically pop out some tags inside the `<form>` and remaining the `<img>` without removing its attributes. To understand this deeper, I still need to need some writeups before about this mXSS, it's kinda new with me.

## References
- https://aszx87410.github.io/beyond-xss/en/ch2/mutation-xss/
- https://mizu.re/post/exploring-the-dompurify-library-bypasses-and-fixes
- https://ensy.zip/posts/dompurify-323-bypass/
- https://yaniv-git.github.io/2024/12/08/DOMPurify%203.2.1%20Bypass%20(Non-Default%20Config)/
- https://jorianwoltjer.com/blog/p/research/mutation-xss
