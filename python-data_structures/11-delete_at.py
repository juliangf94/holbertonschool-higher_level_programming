def delete_at(my_list=[], idx=0):
    copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy
