#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        average = 0
        div = 0
        for tup in my_list:
            average += (tup[0] * tup[1])
            div += (tup[1])
        return (average/div)
    return 0
