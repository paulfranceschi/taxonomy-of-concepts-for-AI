[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Repo Size](https://img.shields.io/github/repo-size/paulfranceschi/taxonomy-of-concepts-for-AI)
# General considerations

<img align="right" width="75%" src="https://github.com/paulfranceschi/taxonomy-of-concepts/blob/main/screen3.jpg">

The aim of this project is to create a library in Python based on a taxonomy of commonly used concepts, so that it can be used for artificial intelligence (AI) improvement. Compelling though it is, in most cases, the GPT model answers questions like these incorrectly:
* With which concept is blissful optimism in the same type of relationship as subjectivity and objectivity?

The answer is: '... perception.' We propose here a set of training data that allow for a response of the type: 'On the one hand, blissful optimism is a negative concept. On the other hand, subjectivity is a negative one and objectivity is a positive concept. Thus, the missing concept is a positive one. Hence, blissful optimism and awareness of problems are in the same relationship as subjectivity and objectivity.'

The structured library that is part of the module is intended to provide the AI with a better grasp of these common concepts, such as courage, cowardice, prudence, optimism, prodigality, inclemency, clemency, objectivity, instability, ambition, etc. As a consequence, it will allow the AI to answer properly to a broad range of questions such as:

* Can you complete the following sentence, where the last word is missing: cowardice and cautiousness are in the same type of relationship as stinginess and ... 
* Can you complete the following sentence, where the last word is missing: prodigality and avarice are in the same type of relationship as inclemency and ...

## Project history
This project was initiated by philosopher [Paul Franceschi](www.paulfranceschi.com) in February 2023.

* v0.992: csv file upload expanded
* v0.99: optimized prompts and completions for fine-tuning
* v0.98: expanded corpus generator and added prompts and completions for fine-tuning
* v0.97: expanded corpus generator
* v0.96: added corpus generator
* v0.95: first version

# Software tools
Software tools are available for this project that consist of:
* a python module
* a set of .csv files that contain the list of concepts organized according to the matrices of concepts' structure. There is one .csv file for each language

## Code generator
The code generator creates python code for the relevant taxonomy of concepts. The code generator starts with a list of concepts organised in a 6-column table, and automatically and instantly generates the corresponding code. To generate this list of concepts, a simple .csv file can be used. The result is a nested python dictionary of concepts which, among other things, makes it possible to determine for each concept its opposite, its complementary concept, etc. In addition, the various concept dictionaries inherent in each language are themselves integrated into a list of dictionaries, resulting in a multilanguage module. In order to determine the opposite of the concept of 'courage' in English, simply type:
dic[ENG]['courage']['2-contrary'] and the result is: 'cowardice'.

## Corpus generator
<img align="right" width="75%" src="https://github.com/paulfranceschi/taxonomy-of-concepts/blob/main/screen-training-data.jpg">
This tool can be used to prepare training data. It allows the design of prompts and completions for fine-tuning.

The corpus genrator is also a citation generator. It allows to create:
* a set of citations based on the taxonomy of concepts
* a corpus of citations, that can notably be used to train an AI

The kinds of citations that are generated are of the following type:
* courage is the contrary of cowardice
* avarice is the contrary of generosity
* firmness is complementary to clemency

# Matrices of concepts
<img align="right" width="30%" src="https://github.com/paulfranceschi/taxonomy-of-concepts/blob/main/matrix-of-concepts.jpg">
The matrix of concepts is a structure that includes six concepts, which is suitable for modeling many common concepts, such as: courage, recklessness, irresolution, eclecticism, superficiality, clemency, instability, selfishness, objectivity, frankness, brusqueness, altruism, etc. Of the six concepts in the matrix:

* two are neutral: A<sup>0</sup> and Ā<sup>0</sup>
* two are positive: A<sup>+</sup> and Ā<sup>+</sup>
* two are negative: A<sup>-</sup> and Ā<sup>-</sup>

These six concepts constitute the canonical poles of the matrix.

The six concepts of the matrix are in particular relationships with each other. Thus:

* the neutral concepts A<sup>0</sup> and Ā<sup>0</sup> are dual
* the positive concept A<sup>+</sup> and the negative concept Ā<sup>-</sup> are opposite (or contrary); similarly, the negative concept A<sup>-</sup>  and the positive concept Ā<sup>+</sup> are opposite (or contrary)
* the positive concepts A<sup>+</sup> and Ā<sup>+</sup> are complementary
* lastly, the negative concepts A<sup>-</sup> and Ā<sup>-</sup> are extreme opposites

<img align="right" width="50%" src="https://github.com/paulfranceschi/taxonomy-of-concepts/blob/main/matrix-of-concepts-instance.jpg">
In the instance of matrix of concepts pictured on the right:

* the propensity to take risks and the propensity to avoid risks are dual
* audacity and cowardice are contrary, opposite; in the same way, temerity and prudence are contrary, opposite
* audacity and prudence are complementary
* temerity and cowardice are extreme opposites

Moreover, the three concepts located on the left of the matrix constitute a half-matrix: it is the half-matrix associated with the pole A. In the same way, the three concepts located on the right of the matrix constitute the half-matrix associated to the pole Ā.

## References
This project is based on the structure of concepts put forth in my paper entitled:
* Franceschi, Paul (2002), ‘Une classe de concepts’, Semiotica 139: 211-226. doi.org/10.1515.semi.2002.020

that introduces the matrices of concepts. An [English translation](https://www.paulfranceschi.com/blog/on-a-class-of-concepts/) is also available.

# How to contribute?
You can contribute to the project in different ways:
* by completing, enriching or correcting the concepts' lists. They are presented as .csv files (in utf8 format), so that their structure is easily accessible and understandable without any specialised computer knowledge.
* by translating the concepts' lists into toher languages. Endangered languages are very welcome.
* by participating in the development of the software tools associated with the project. 

# A multilingual project
This project is intended to be multilingual and provides the tools for its extension to other languages. Endangered languages are especially welcome.

# License
This project is published under the MIT license. 

# Acknowledgements
Icons are from:
* [ogygen-icons](https://github.com/KDE/oxygen-icons)
* and from [tango-icon-library](https://github.com/freedesktop/tango-icon-library)

