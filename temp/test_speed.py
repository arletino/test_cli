import timeit
from memory_profiler import profile

test_list = [1 for _ in range(10_000_000)]
test_tuple = tuple(test_list)
@profile
def calc_sum(sequence):
    res = 0
    for x in sequence:
        res += x

    return res

time_tuple = timeit.timeit("calc_sum(test_tuple)", globals=globals(), number=5)
print(f"{time_tuple=}")
time_list = timeit.timeit("calc_sum(test_list)", globals=globals(), number=5)
print(f"{time_list=}")
