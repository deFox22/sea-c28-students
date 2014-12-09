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
