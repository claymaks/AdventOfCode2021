# Part 1
with open("../input", 'r') as f:
    position = [0, 0]

    for cmd, units in map(lambda x: x.split(' '), f.readlines()):
        units = int(units)
        if cmd == "forward":
            position[0] += units
        else:
            position[1] += (-1 if cmd == "up" else 1 if cmd == "down" else 0) * units

print("What do you get if you multiply your final horizontal position by your final depth?")
print(f"Answer: {position[0]}x{position[1]} = {position[0] * position[1]}")

# Part 2
with open("../input", 'r') as f:
    position = [0, 0, 0]

    for cmd, units in map(lambda x: x.split(' '), f.readlines()):
        units = int(units)
        if cmd == "forward":
            position[0] += units
            position[1] += position[2] * units
        elif cmd == "down":
            position[2] += units
        elif cmd == "up":
            position[2] -= units
        else:
            print(f"Unknown command: {cmd}")

print("What do you get if you multiply your final horizontal position by your final depth?")
print(f"Answer: {position[0]}x{position[1]} with aim {position[2]} = {position[0] * position[1]}")
