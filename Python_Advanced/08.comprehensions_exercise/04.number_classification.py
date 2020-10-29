num = [int(x) for x in input().split(", ")]

positive = [str(x) for x in num if x >= 0]
negative = [str(x) for x in num if x < 0]
even = [str(x) for x in num if x % 2 == 0]
odd = [str(x) for x in num if x % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
