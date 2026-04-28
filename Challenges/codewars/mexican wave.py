def wave(people: str):
    sequence = []
    for n in range(len(people)):
        if people[n] == " ":
            n+=1
        else:
            sequence.append(people[:n] + people[n].upper() + people[n+1:])
    return sequence