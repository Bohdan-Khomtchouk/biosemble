#!/usr/bin/env python

# Copyright (C) 2017 Bohdan Khomtchouk
# This file is part of biosemble.

# -------------------------------------------------------------------------------------------

from nltk import word_tokenize, pos_tag
from collections import defaultdict
import json
import glob


final_results = defaultdict(set)
for f_name in glob.glob('NCI/*.json'):
	print(f_name)
	with open(f_name) as f:
		temp_d = json.load(f)
	for word, desc in temp_d.items():
		nouns = set()
		for w, tag in pos_tag(word_tokenize(desc)):
			if 'NN' in tag and len(w) > 2:
				nouns.add(w)
		final_results[word] |= nouns

final_results = {word: list(sims) for word, sims in final_results.items()}
with open("final_result.json", 'w') as f:
	json.dump(final_results, f, indent=4)