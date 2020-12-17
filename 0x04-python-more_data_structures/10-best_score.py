def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    sort = sorted(a_dictionary.values())
    maxval = sort[-1]
    for i in a_dictionary:
        if a_dictionary[i] == maxval:
            return i
