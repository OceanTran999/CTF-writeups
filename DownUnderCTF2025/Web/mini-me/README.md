First, when accessing the `main.min.js` JS file, I see there's another JS file that's not produced orignally, called `test-main.min.js.map`.

Then using `sourcemap` tool to change the `.map` file into original `.js` file in order to easily analysize JS file source code.

After having `.js` file, copy the `qyrbkc()` file into the browser. Change the line code `console.log()` to print the `lmsvdt` variable, which contains the value of api key.

Reading the `app.py`, we see that we have to use `POST` method and including the `X-API-KEY` in the HTTP header to get the flag.