d = {}

while True:
    stop = input()
    if stop == "Sail":
        break
    spl = stop.split("||")
    townn = spl[0]
    peoplee = int(spl[1])
    gold = int(spl[2])

    if townn not in d.keys():
        d[townn] = [peoplee, gold]
    elif townn in d.keys():
        d[townn][0] += peoplee
        d[townn][1] += gold

while True:
    text = input()
    if text == "End":
        break
    sp = text.split("=>")
    if sp[0] == "Plunder":
        town = sp[1]
        people = int(sp[2])
        gold = int(sp[3])
        if d[town][0] <= people or d[town][1] <= gold:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            del d[town]
            print(f"{town} has been wiped off the map!")
        else:
            d[town][1] -= gold
            d[town][0] -= people
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    elif sp[0] == "Prosper":
       city = sp[1]
       gold = int(sp[2])
       if gold > 0:
           d[city][1] += gold
           print(f"{gold} gold added to the city treasury. {city} now has {d[city][1]} gold.")
       else:
           print("Gold added cannot be a negative number!")

if d:
    print(f"Ahoy, Captain! There are {len(d)} wealthy settlements to go to:")
    p = sorted(sorted(d), key= lambda x: d[x][1],reverse=True)
    for j in p:
        print(f"{j} -> Population: {d[j][0]} citizens, Gold: {d[j][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")










