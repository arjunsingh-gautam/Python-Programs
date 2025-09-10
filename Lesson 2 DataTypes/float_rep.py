# This program show how python stores float values internally IEEE 754 standard using 64 bits

import struct

num = 1.23e12
packed = struct.pack('>d', num)  # '>d' = big-endian double
print("Binary:", ''.join(f'{byte:08b}' for byte in packed))

