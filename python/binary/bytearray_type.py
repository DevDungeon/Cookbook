mutable_bytes = bytearray(b'\xFF\x0F')
print(mutable_bytes)

mutable_bytes[1] = 255
mutable_bytes.append(128)
print(mutable_bytes)
print(type(mutable_bytes))

immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)
print(type(immutable_bytes))
