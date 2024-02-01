#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxScore, maxKey = None, None
    for key in a_dictionary:
        if maxScore == None:
            maxScore = a_dictionary[key]
            maxKey = key
            continue
        if maxScore < a_dictionary[key]:
            maxScore = a_dictionary[key]
            maxKey = key
    return maxKey
