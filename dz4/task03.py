def pop_repeats(list_):
    list_step = set(list_)
    list_end = list(list_step)
    return list_end


list_start = list(map(int, input().split()))
print(pop_repeats(list_start))
