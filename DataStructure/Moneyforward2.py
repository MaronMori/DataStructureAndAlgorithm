values = input().split(" ")
point = int(values[0])
bonus = int(values[1])
goal = int(values[2])

days = 0
total = point

while total < goal:
    days += 1

    total += point

    if "7" in str(days):
        total += bonus

print(days)
