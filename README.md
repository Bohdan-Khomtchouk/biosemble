<div align="center">

# biosemble

<img src="https://user-images.githubusercontent.com/9893806/31262867-fd454414-aa12-11e7-8ada-c7867c4103be.png">

### AI assembly of biological wordnets

</div>

## About

`biosemble` is a Python natural language processing (NLP) software program for assembling biological wordnets from structured and unstructured biological text.  Structured text includes resources like biologically relevant dictionaries and encyclopedias, while unstructured text includes biologically relevant textbooks.

## How good is it?

`biosemble` can autonomously identify leukemia as a blood cancer, and CD38 as a glycoprotein on the cell surface that is relevant to leukemia:

<img width="971" alt="biological_wordnet" src="https://user-images.githubusercontent.com/9893806/31262996-0562c6fc-aa14-11e7-9119-2bbfc45f1e1a.png">

Not too bad!

## Algorithms

### Structured biological text

`biosemble` uses part-of-speech (POS) tagging to assemble similar words across a wide array of biologically relevant dictionaries and encyclopedias.  

### Unstructured biological text<sup>1</sup>

`biosemble` uses Word2Vec which is a Neural Network based algprithm to produce a group of related models that are used to produce word embeddings. Using `biosemble` you can pass in your custom argumetns based on the input data, required to generate the most precise results.
 

## Citation
Coming soon!

