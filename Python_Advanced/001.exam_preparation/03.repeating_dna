from collections import deque


def get_repeating_DNA(letter):
    save = ''
    dna_save = deque()
    total = []
    count = 0
    while len(letter) >= 10:
        dna_save.append(letter[0:10])
        letter = letter[1:]  

    while len(dna_save) > 0:
        first = dna_save.popleft()
        if first in dna_save:
            if first not in total:
                total.append(first)

    return total
