text = input().split('\\')

last = text[-1]

spl = last.split(".")

print(f"File name: {spl[0]}")
print(f"File extension: {spl[1]}")
