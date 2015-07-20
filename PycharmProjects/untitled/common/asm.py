__author__ = 'KamilLeszekP'

def pr_find_duplicates(sort_dict):
    keys = sort_dict.keys()
    dict_duplicates = dict()
    n = len(keys)
    for i in range(len(keys)-1):
        found = 0
        for j in range(i+1, n):
            if sort_dict[keys[i]] == sort_dict[keys[j]]:
                if found == 0:
                    dict_duplicates[keys[i]] = sort_dict[keys[i]]
                    found = found + 1
                dict_duplicates[keys[j]] = sort_dict[keys[j]]
                #print keys[i] + ' cos tam ' + keys[j]
    return dict_duplicates