# Get the power set for a given list, 2**len(list) subsets
def get_powerset(super_set):
    power_set = []
    for i in range(2**len(super_set)):
        sub_set = []
        for index,val in enumerate(super_set):
            if ((i>>index) & 1):
                sub_set.append(val)
        power_set.append(sub_set)
    yield power_set