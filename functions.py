import pickle
import os

# removes values corresponding to "unknown"
def remove_unknown(lst):
    lst = list(set(lst))
    for item in [0,500,768]:
        if item in lst:
            lst.remove(item)
        if len(lst)==0:
            return [0]
        else:
            return lst

# changes sick code to classified idx
def get_classified_sickness(sample):
    if len(sample)<3:
        return 0
    c, num = sample[0], int(sample[1:])
    with open('/home/mjc/github/EHRVis/data/dictionaries/sick_converter.pckl','rb') as f:
        s2i = pickle.load(f)
    for i, rng in enumerate(s2i[0][c]):
        if '-' in rng:
            lower, upper = rng.split('-')
            lower = int(lower[1:])
            upper = int(upper[1:])
            if (lower<=num) & (upper>=num):
                answer = s2i[1][c][i]
                return answer
        else:
            if num==int(rng[1:]):
                answer = s2i[1][c][i]
                return answer
            else:
                return 0

# get_batch function for preprocessing the list of a single user
def list_to_inputs_targets(input_list):
    inputs = []
    targets = []
    for tup in input_list:
        inputs.append(tup[2])
        targets.append(tup[3])
    return inputs, targets
