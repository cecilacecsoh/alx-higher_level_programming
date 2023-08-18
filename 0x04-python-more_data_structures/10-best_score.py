#!/usr/bin/python3

def best_score(cec_dictionary):
    return max(cec_dictionary, key=cec_dictionary.get) if cec_dictionary else None
