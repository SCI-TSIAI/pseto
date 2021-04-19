data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

print(data)
for b in data:
    print(hex(b))