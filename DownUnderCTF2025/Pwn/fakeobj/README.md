Here are some `ctypes` functions that I read from the Python docs.

- `ctypes.c_void_p`: Represents the C void* type. The value is represented as integer. The constructor accepts an optional integer initializer.

- `ctypes.cast(obj, type)`: This function is similar to the cast operator in C. It returns a new instance of type which points to the same memory block as obj. type must be a pointer type, and obj must be an object that can be interpreted as a pointer.

- `ctypes.POINTER(type, /)`: Create or return a ctypes pointer type. Pointer types are cached and reused internally, so calling this function repeatedly is cheap. type must be a ctypes type.

First, the `system()` will be assigned as a `void*` type pointer.

Then it will handle a loop with 72 1-byte elements, the `cast()` function I understand that it likes:

```
    (char*) id_obj[i] = fakeobj_data[i]   // id_obj is Integer value
```

**Note**: Because the program uses `bytes.fromhex` to receive hexadecimal string and convert them to byte, so our payload must be convert to hex string first and send to the server.

I read a writeup that has information about CPython to exploit the print() function when calling an object: https://blog.kittycar.online/posts/2025/07/20/ductf-2025-fakeobject/