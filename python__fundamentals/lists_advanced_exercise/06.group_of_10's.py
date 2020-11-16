numbers = list(map(int, input().split(", ")))
group = 10


while len(numbers) > 0:
    filtred = [num for num in numbers if num <= group]
    numbers = [num for num in numbers if num > group]
    print(f"Group of {group}'s: {filtred}")
    group += 10
