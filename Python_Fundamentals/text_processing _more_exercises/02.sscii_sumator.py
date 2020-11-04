start = input()
stop = input()

text = input()

total = 0
s = ord(start)
f = ord(stop)

for letter in text:
    o = ord(letter)

    if o > s and o < f:
        total += o

print(total)
