# Part 1
with open("../input", 'r') as f:
    log = None

    for num in f.readlines():
        num = num.replace('\n', '')
        if log is None:
            log = {i: {'0': 0, '1': 0} for i in range(len(num))}
        for n, digit in enumerate(num):
            log[n][digit] += 1

gamma = ""
epsilon = ""
for i in range(len(log)):
    gamma += '0' if log[i]['0'] > log[i]['1'] else '1'
    epsilon += '1' if log[i]['0'] > log[i]['1'] else '0'
    

gamma_int = int("0b" + gamma, base=2)
epsilon_int = int("0b" + epsilon, base=2)
        
print("What is the power consumption of the submarine?")
print(f"Answer: {gamma}x{epsilon} = {gamma_int * epsilon_int}")

# Part 2
with open("../input", 'r') as f:
    lines_master = f.readlines()

    lines = lines_master.copy()
    desired_o = ""

    for n in range(len(lines[0].replace('\n', ''))):
        log = {'1': 0, '0': 0}
        for num in lines:
            num = num.replace('\n', '')
            
            # count digits
            log[num[n]] += 1
            
        desired_o += '0' if log['0'] > log['1'] else '1'
        lines = [line for line in lines if line.startswith(desired_o)]
        if len(lines) == 1:
            desired_o = lines[0].replace('\n', '')
            break

    lines = lines_master.copy()
    desired_co2 = ""

    for n in range(len(lines[0].replace('\n', ''))):
        log = {'1': 0, '0': 0}
        for num in lines:
            num = num.replace('\n', '')
            
            # count digits
            log[num[n]] += 1
        desired_co2 += '1' if log['1'] < log['0'] else '0'
        lines = [line for line in lines if line.startswith(desired_co2)]
        if len(lines) == 1:
            desired_co2 = lines[0].replace('\n', '')
            break


desired_o_int = int("0b" + desired_o, base=2)
desired_co2_int = int("0b" + desired_co2, base=2)
    
print("What is the life support rating of the submarine?")
print(f"Answer: {desired_o}x{desired_co2} = {desired_o_int * desired_co2_int}")
