def convert_to_little_endian(hex):
    # Left to right
    right1 = (hex & 0xff00000000000000) >> 56
    right2 = (hex & 0x00ff000000000000) >> 40
    right3 = (hex & 0x0000ff0000000000) >> 24
    right4 = (hex & 0x000000ff00000000) >> 8

    # Right to left
    left1 = (hex & 0xff) << 56
    left2 = (hex & 0xff00) << 40
    left3 = (hex & 0xff0000) << 24
    left4 = (hex & 0xff000000) << 8

    return right1 | right2 | right3 | right4 | left1 | left2 | left3 | left4


list_byte = [0x4152447b4654434b, 0x6c4f7243734e4f47, 0x7d6c]
for i in range(len(list_byte)):
    value = hex(convert_to_little_endian(list_byte[i])).replace('0x', '')
    print(value, end='')