#!/usr/bin/python3
def best_score(dict):
    if dict and len(dict):
        max = list(dict.keys())[0]
        for key in dict:
            if dict[key] > dict[max]:
                max = key
        return max
    return None
