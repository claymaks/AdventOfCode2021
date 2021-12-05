import os
import sys
import random

PROB = 0.05
    
if 'idlelib.run' not in sys.modules:
    def solution(part, x):
        l = len(f"Part {part}: {x}")
        print(" " * max((w//3) - (2 * l//3), 0) + f"\x1b[0m\x1b[31m\x1b[1m Part {part}: \x1b[22m{x}", end='' if part == 1 else '\n')
    

    w, h = os.get_terminal_size()
    from colorama import Fore, Back, Style

    def snow(prob=0.05):
        if random.random() < prob:
            return "\x1b[2m\x1b[36m*"
        return " "
            

    def snow_line(w, prob=0.05):
        s = ""
        for i in range(w):
            s += snow(prob=prob)
        return s    
    
    print(''.join([snow_line(w, prob=PROB) + "\n" for _ in range(max(h - 15, 0))]))

    f = open("tree.txt", 'r')
    for line in f.readlines():
        print(snow_line(max((w//2) - 5, 0), prob=PROB) + line.replace('\n', '') + snow_line(max((w//2) - 6, 0), prob=PROB))
    f.close()
    
else:
    def solution(part, x):
        print(f" Part {part}: {x}")
        
    print("""
    _\\/_
     /\\
     /\\
    /  \\
    /~~\\o
   /o   \\
  /~~~~~~\\
 o/    o \\
 /~~~~~~~~\\o
/__o_______\\
     ||
   \\====/
    \\__/
""")




