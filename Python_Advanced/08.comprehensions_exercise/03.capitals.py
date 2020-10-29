country = input().split(", ")
capital = input().split(", ")


dictionary = {key: value for (key, value) in zip(country, capital)}

[print(f"{key} -> {value}") for (key, value) in dictionary.items()]
