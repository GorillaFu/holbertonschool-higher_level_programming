#!/usr/bin/python
def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    i = len(sentence)
    j = sentence[0]
    return i, j
