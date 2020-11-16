electrons = int(input())

shells = []
shell_idx = 1

while electrons > 0:
    max_electrons = 2 * shell_idx ** 2
    if max_electrons >= electrons:
        shells.append(electrons)
        electrons -= max_electrons
    else:
        shells.append(max_electrons)
        electrons -= max_electrons
    shell_idx += 1

print(shells)
