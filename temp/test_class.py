from random import randint


num=10_000_000

# def create_tuple(num):
#     return tuple([randint(1, 10) for _ in range(num)])

def create_lst(num):
    return [randint(1, 10) for _ in range(num)]

# tpl = create_tuple(num=num)
lst = create_lst(num=num)

def iter_seq(some):
    """Stupid test function"""
    l = [i for i in some]

if __name__=='__main__':
    import timeit
    # tm_tpl =timeit.timeit('iter_seq(tpl)', globals=globals(), number=10)
    tm_lst = timeit.timeit('iter_seq(lst)', globals=globals(), number=10)
    # print('tuple-', tm_tpl)
    print('list-', tm_lst)