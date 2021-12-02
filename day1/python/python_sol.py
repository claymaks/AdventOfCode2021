# Part 1
with open("../input", 'r') as f:
    # Read in our first measurement.
    num_increased = 0
    last_measurement = int(f.readline())

    # Iterate through remaining measurements, incrementing counter if the depth
    # has increased. 
    for line in f.readlines():
        measurement = int(line)
        if measurement > last_measurement:
            num_increased += 1
        last_measurement = measurement

print("How many measurements are larger than the previous measurement?")
print(f"Answer: {num_increased}")

# Part 2
with open("../input", 'r') as f:
    # Read in first three measurements.
    num_increased = 0
    window = [int(f.readline()) for _ in range(3)]

    # Iterate through remaining measurements, sliding window and comparing it to
    # the previous window. Increment the counter if the sum of the window has
    # increased.
    for line in f.readlines():
        last_sum = sum(window)
        window = window[1:] + [int(line)]
        
        if sum(window) > last_sum:
            num_increased += 1

print("How many sums are larger than the previous sum?")
print(f"Answer: {num_increased}")
