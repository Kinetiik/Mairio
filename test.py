a = [0, 1, 1, 0, 0, 1, 1, 0]
binary = ""
for i in range(8):
    binary += str(a[i])

b = int(binary, 2)

bin = list(format(b, "b"))



while len(bin) < 8:
    bin.insert(0, 0)
    
bin = list(map(int, bin))
print(bin)
print(bin == a)
