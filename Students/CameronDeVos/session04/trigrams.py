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


def write_story(trigrams):
    u"""Return a new story from the dictionary of trigrams"""
    new_story = ""
    random_key = random.choice(trigrams.keys())
    current_word = (random_key[0], random_key[1])
    last_word = random_key[1]
    new_story += ' {0} {1}'.format(random_key[0], random_key[1])
    for i in range(story_length(sherlock_data)):
        if current_word in trigrams.keys():
            # Pull values for key with last 2 words
            value_picklist = trigrams[current_word]
            # Pick value at random
            random_value = random.choice(value_picklist)
            # Add value to story
            if str(random_value).istitle():
                new_story += '. {0}'.format(random_value)
            else:
                new_story += ' {0}'.format(random_value)
            # Update current word key to match last 2 words of story
            last_word = current_word[1]
            current_word = (last_word, random_value)
        else:
            new_story += (u". The End!")
            break
    return new_story

sherlock.close()

if __name__ == '__main__':

    word_list = create_word_list(sherlock_data)
    trigrams = create_trigrams(word_list)
    new_story = write_story(trigrams)
    print (new_story)
