def rev_byte(target:hex):
    left = (target & 0xff000000) >> 24
    mid1 = (target & 0xff0000) >> 8
    mid2 = (target & 0xff00) << 8
    right = (target & 0xff) << 24
    return left | mid1 | mid2 | right

hex_target = '65646f43-74736566-7b465443-6d723066-355f7434-6e317237-336c5f67-695f6b34-41625035-7d50506b'
hex_list = hex_target.split('-')

for i in range(0, len(hex_list)):
    rev_num = rev_byte(int(hex_list[i], 16))
    print(hex(rev_num))