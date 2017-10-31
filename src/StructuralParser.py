#!/usr/bin/env python

# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------

from nltk import word_tokenize, pos_tag
from collections import defaultdict
import json
import glob


class WordNet:
    def __init__(self, **kwargs):
        self.data_path = kwargs['data_path']
        self.wordnet_path = kwargs['wordnet_path']
        self.wordnet_name = kwargs['wornet_name']

    def parser(self):
        """Accepts the structured data as a JSON. It contains a word and
        its respective description."""

        wordnet = defaultdict(set)
        with open(self.data_path) as f:
            temp_d = json.load(f)
            for word, desc in temp_d.items():
                nouns = set()
                for w, tag in pos_tag(word_tokenize(desc)):
                    if 'NN' in tag and len(w) > 2:
                        nouns.add(w)
                wordnet[word] |= nouns
        return wordnet

    def create_wordnet(self):
        wordnet = {word: list(sims) for word, sims in self.parser().items()}
        with open("{}.json".format(self.wordnet_name), 'w') as f:
            json.dump(wordnet, f, indent=4)
