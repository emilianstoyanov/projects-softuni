words_stgrins = input().split(" ")
palindrome = input()

palimdromes = [word for word in words_stgrins if word == word[::-1]]
palindrome_count = palimdromes.count(palindrome)

print(palimdromes)
print(f"Found palindrome {palindrome_count} times")
