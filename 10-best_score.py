#!/usr/bin/python3
def best_score(a_dictionary):
    high_score = a_dictionary[0]
    for i in a_dictionary:
        if a_dictionary[i] > high_score:
            high_score = a_dictionary[i]
            return high_score
  
