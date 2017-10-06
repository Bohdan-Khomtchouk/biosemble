#!/usr/bin/env python

# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------

import json
from nltk import word_tokenize, pos_tag
import codecs
from itertools import chain


class Corpus():
    def __init__(self, *args, **kwargs):
        self.input_file = kwargs['input_file']
        self.output_file = kwargs['output_file']

    def create_dict(self):
        with codecs.open(self.input_file, encoding='UTF-8') as f:
            words = json.load(f)
        new_dict = {k: [word for word, tag in pos_tag(list(chain.from_iterable([word_tokenize(i.replace('- ', '')) for i in v]))) 
                    if 'NN' in tag and len(word) > 3] for k, v in words.items()}
        return new_dict

    def create_json(self):
        tagged_dict = self.create_dict()
        with codecs.open(self.output_file, 'w', encoding='UTF-8') as f:
            json.dump(tagged_dict, f, indent=4)


if __name__ == "__main__":
    Crp = Corpus(input_file='all_words.json',
                 output_file='corpus.json')
    Crp.create_json()
