import sys
import time

def day_1(input_file):
    best = person = 1
    best_sum = total = 0
    with open(input_file) as f:
        for line in f:
            if len(line) <= 1:
                if total > best_sum:
                    best_sum = total
                    best = person
                person += 1
                total = 0
            else:
                val = int(line)
                total += val
        if total > best_sum:
            return person, total
        return best, best_sum

if __name__ == '__main__':
    start_day_1 = time.time()
    day_1(sys.argv[1])
    print(f"Part 1: {time.time() - start_day_1:.10f} seconds")

    #start_part_2 = time.time()
    #part_2(sys.argv[1])
    #print(f"Part 2: {time.time() - start_part_2:.3f} seconds")