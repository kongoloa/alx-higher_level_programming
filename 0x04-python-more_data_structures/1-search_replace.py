#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def src(x):
        return (x if x != search else replace)
    return list(map(src, my_list))
