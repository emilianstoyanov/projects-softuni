words = input().split(" ")
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")







# def solve(words_str):
#     words = [word.lower() for word in words_str.split(" ")]
#     words_occurrences = {}
#     for word in words:
#         if word not in words_occurrences:
#             words_occurrences[word] = 0
#         words_occurrences[word] += 1
#
#     odd_words = [word for (word, count)
#                  in words_occurrences.items()
#                  if count % 2 == 1]
#
#     print(" ".join(odd_words))
#
# tests = [input()]
#
# [solve(test) for test in tests]
