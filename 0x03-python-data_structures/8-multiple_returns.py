#!/bin/python

def multiple_returns(sentence):
    length_sentence = len(sentence)
    if length_sentence < 0:
        return (length_sentence, None)
    else:
        return(length_sentence, sentence[0])
