#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]  # filter even numbers only

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]  # add exclamation to each