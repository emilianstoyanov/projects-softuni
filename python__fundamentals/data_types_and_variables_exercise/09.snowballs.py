snowball = int(input())
output_string = ""
max_snowball_value = -99999
for i in range(snowball):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow // snowball_time) ** snowball_quality
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        output_string = f"{snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})"

print(output_string)

