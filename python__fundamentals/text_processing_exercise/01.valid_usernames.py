text = input().split(", ")

for word in text:
    if 3 <= len(word) <= 16 and (word.isalnum() or "_" in word or "-" in word): 
        print(word)
