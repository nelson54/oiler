from time import time
start_time = time()

from itertools import permutations
from copy import copy

number_of_batches = 20
normal_success_of_batch = 17
sample = 5

pool = [1 for x in range(normal_success_of_batch)] + \
       [0 for y in range(number_of_batches - normal_success_of_batch)]

all_permutations = permutations(pool, sample)
all_permutations_count = sum(1 for a in copy(all_permutations))

passes_count = sum(1 for b in filter(lambda x: x >= 4, map(lambda x: sum(x), all_permutations)))

print("Of", all_permutations_count, "permutations there were", passes_count, "passes.")
print("Probability of success:", passes_count/all_permutations_count)

print("--- %s seconds ---" % (time() - start_time))