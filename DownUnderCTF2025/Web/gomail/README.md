There's an Integer Overflow in `WriteEmail()` in `claims.go` file. This bug indicates that we can truncate the `email` field in HTTP POST Request by making the value of `length` into `0`. Abusing Integer Overflow, we will send our request with the length size is `65535 + 1`.

When `/login`, our request will be encoded by `serialize()` our json data to create an authenticated token, because our length is `0`, so it will encode the `mc-fat@monke.zip` email instead the `guest` email as default. Our payload will be:
1) the `mc-fat@monke.zip` email.
2) 8-byte for overwrite the `Expiry` value.
3) 1-byte for overwriting the `isAdmin` value (change from `f` to `t`).
4) And the remaining data to make our request's length is `65536`.

After getting our token, send to the `/email` we will get the flag.