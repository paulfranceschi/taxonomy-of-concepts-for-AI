# General considerations

<img align="right" width="75%" src="https://github.com/paulfranceschi/taxonomy-of-concepts/blob/main/screen.jpg">

The aim of this project is to create a library in Python based on a taxonomy of commonly used concepts, so that it can be used in projects related to artificial intelligence (AI) and natural language understanding. The library that is part of the module is intended to allow an AI to answer a broad range of questions such as:

* What is the opposite of generosity? What is the contrary of audacity?

## project history
This project was initiated by philosopher [Paul Franceschi](www.paulfranceschi.com) in February 2023.

# Software tools
Software tools are available for this project that consist of:
* a python module
* a set of .csv files that contain the organized list of concepts, one for each language

## code generator
The code generator creates python code for the relevant taxonomy of concepts. The code generator starts with a list of concepts organised in a 6-column table, and automatically and instantly generates the corresponding code. To generate this list of concepts, a simple .csv file can be used. The result is a nested python dictionary of concepts which, among other things, makes it possible to determine for each concept its opposite, its complementary concept, etc. In addition, the various concept dictionaries inherent in each language are themselves integrated into a list of dictionaries, resulting in a multilanguage module.

## corpus generator
This tool is a citation generator. It allows to create:
* a set of citations based on the taxonomy of concepts
* a corpus of citations, that can notably be used to train an AI

# How to contribute?
You can contribute to the project by completing, enriching or correcting the dictionaries, or by participating in the development of the software tools associated with the project. The dictionaries are presented as .csv files, so that their structure is easily accessible and understandable without any specialised computer knowledge.

# A multilingual project
This project is intended to be multilingual and provides the tools for its extension to other languages. Endangered languages are especially welcome.

# License
<img align="right" width="35%" src="https://github.com/paulfranceschi/taxonomy-of-concepts/blob/main/matrix of concepts.jpg">

This project is published under the MIT license.

# References
This project is based on the structure of concepts put forth in my paper entitled:
* Franceschi, Paul (2002), ‘Une classe de concepts’, Semiotica 139: 211-226. doi.org/10.1515.semi.2002.020

that introduces the matrices of concepts. An English translation is also available:
* https://www.paulfranceschi.com/blog/on-a-class-of-concepts/
