import time
import random
import string
import pickle
import numpy as np
from nltk import pos_tag

class DrumpfTweetWriter():
    '''
    This will write tweets in the style of... the 45th president of the United
    States.

        n_grams - this sets the ngrams to use, 1, 2, or 3
        char_limit - this sets the character limit, 1 = 140, 2 = 280
        topic - a word to stay on topic, default is 'sad'
        topic_check - number of words to check to stay on topic, default is 2
    '''

    def __init__(self, model, n_grams=2, char_limit=2, topic="sad",
                 topic_check=2):
        self.f = open('data/data.txt')
        self.n_gram = n_grams
        self.char_limit = (char_limit * 135)
        self.topic = topic.lower()
        self.topic_n = topic_check
        self.model = model

    def associated_unigrams(self, f):
        '''
        INPUT: file
        OUTPUT: dictionary

        Return a dictionary where the keys are words in the file inside a tuple
        and the value for each key is a list of words that were found directly
        following the key.

        Words should be included in the list the number of times they appear.

        Suggestions on how to handle first word: create an entry in the dictionary
        with a first key (None)

        Example:
        >>> with open('../data/alice.txt') as f:
        ...     d = associated_unigrams(f)
        >>> d[('among')]
        ['the', 'those', 'them', 'the', 'the', 'the', 'the']
        '''
        text = f.read()
        text = text.split()
        dct = {}
        for n in range(len(text)-1):
            a = self.letters_only(text[n])
            b = self.letters_only(text[n+1])
            try:
                dct[(a)].append(b)
            except:  # failure...
                dct[(a)] = [b]
        return dct

    def associated_bigrams(self, f):
        '''
        INPUT: file
        OUTPUT: dictionary
        '''
        text = f.read()
        text = text.split()
        dct = {}
        for n in range(len(text)-2):
            a = (self.letters_only(text[n]), self.letters_only(text[n+1]))
            b = self.letters_only(text[n+2])
            try:
                dct[(a)].append(b)
            except:  # failure...
                dct[(a)] = [b]
        return dct

    def associated_trigrams(self, f):
        '''
        INPUT: file
        OUTPUT: dictionary

        Return a dictionary where the keys are tuples of three consecutive words in
        the file and the value for each key is a list of words that were found
        directly following the key.

        Words should be included in the list the number of times they appear.
        '''
        text = f.read()
        text = text.split()
        dct = {}
        for n in range(len(text)-3):
            a = (self.letters_only(text[n]),
                 self.letters_only(text[n + 1]),
                 self.letters_only(text[n + 2]))
            b = self.letters_only(text[n + 3])
            try:
                dct[(a)].append(b)
            except:  # failure...
                dct[(a)] = [b]
        return dct

    def letters_only(self, input_string):
        '''
        Returns only letters...and whatever else I set here.
        '''
        good = "abcdefghijklmnopqrstuvwxyz1234567890'.-?!"
        input_string = input_string
        lst = [a for a in input_string]
        return ''.join(lst)

    def get_cos_sim(self, word):
        ret = 0
        if self.topic_n == 1:
            ret = (random.randint(0,3) + random.randint(0,3))/7
        else:
            try:
                ret = self.model.wv.similarity(self.topic, word)
            except:
                ret = 0.0
        return ret

    def hit_send(self):

        '''
        Does the actual thing.
        '''
        n_gram = self.n_gram
        if n_gram == 1:
            dct = self.associated_unigrams(self.f)
        elif n_gram == 2:
            dct = self.associated_bigrams(self.f)
        else:
            dct = self.associated_trigrams(self.f)
        lst = []
        start = 0 - n_gram

        keys = list(dct.keys())
        # if n_gram == 1:
        #     lst = [random.choice(keys)]
        # else:
        #     lst = list(random.choice(keys))
        chars = 0
        while chars < self.char_limit:
            try:
                if n_gram == 1:

                    a_tuple = (lst[-1])
                else:
                    a_tuple = tuple(lst[start:])
                b_lst = dct[a_tuple]
                c_lst = np.random.choice(b_lst, self.topic_n)
                sims = [self.get_cos_sim(a) for a in c_lst]
                lst.append(c_lst[sims.index(max(sims))])
            except:
                if n_gram == 1:
                    lst = lst + [random.choice(keys)]
                else:
                    lst = lst + list(random.choice(keys))
            chars = len(list(' '.join(lst)))

        while chars > (self.char_limit/135)*140:
            chars -= len(lst[-1])
            lst.pop()
        return ' '.join(lst)
