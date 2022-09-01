#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    weight = 0
    score_weight = 0
    for i in range(len(my_list)):
        tuple = my_list[i]
        weight += tuple[1]
        score_weight += tuple[0] * tuple[1]
     return float(score_weight / weight)
