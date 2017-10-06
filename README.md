<div align="center">

# biosemble

<img src="https://user-images.githubusercontent.com/9893806/31262867-fd454414-aa12-11e7-8ada-c7867c4103be.png">

### AI assembly of biological wordnets

</div>

## About

`biosemble` is a Python natural language processing (NLP) software program written in highly-tuned Cython and optimized Python for assembling biological wordnets from structured and unstructured biological text.  Structured text includes resources like biologically relevant dictionaries and encyclopedias, while unstructured text includes biologically relevant textbooks.

## How good is it?

`biosemble` can autonomously identify leukemia as a blood cancer, and CD38 as a glycoprotein on the cell surface that is relevant to leukemia:

<img width="971" alt="biological_wordnet" src="https://user-images.githubusercontent.com/9893806/31262996-0562c6fc-aa14-11e7-9119-2bbfc45f1e1a.png">

Not too bad!

## Algorithms

### Structured biological text

`biosemble` uses part-of-speech (POS) tagging to assemble similar words across a wide array of biologically relevant dictionaries and encyclopedias.  

### Unstructured biological text<sup>1</sup>

`biosemble` uses the following formula for calculating the similarity between any two distinct entities to extract similar words from plain text:

![image](https://cloud.githubusercontent.com/assets/5694520/21303565/5e4c1c5c-c5d4-11e6-95fe-3e434c1a3b21.png)

![image](https://cloud.githubusercontent.com/assets/5694520/21303577/79b0bd5e-c5d4-11e6-84dd-0b8343ee70b0.png)


Where affinity is defined as follows:

![image](https://cloud.githubusercontent.com/assets/5694520/21303883/c74fe9a2-c5d6-11e6-8634-d2e212ff5b32.png)

![image](https://cloud.githubusercontent.com/assets/5694520/21303889/d435c68c-c5d6-11e6-8334-8d88e20529d4.png)

## Citation
Coming soon!

-------------
<sub>
1. Yael Karov and Shimon Edelman. 1998. Similarity-based word sense disambiguation.
*Computational Linguistics, 24(1):41-59.*
</sub>
