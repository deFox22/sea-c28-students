#!/usr/bin/python

from __future__ import print_function
import io
import string
import random

sherlock = io.open('short_sherlock.txt', encoding='utf-8')
sherlock_data = sherlock.read()


def create_word_list(txtfile):
    u"""Return a list of words from the input txtfile"""
    words = []
    for word in txtfile.split():
        word = word.strip(string.punctuation + string.whitespace)
        words.append(word)
    return words


def story_length(words):
    u"""Return the count of words from the input word list"""
    return len(create_word_list(words))


def create_trigrams(words):
    u"""Return a dictionary of trigrams from the input word list"""
    trigrams = {}
    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        value = words[i+2]
        if key in trigrams:
            trigrams[key].append(value)
        else:
            trigrams[key] = [value]
    return trigrams
