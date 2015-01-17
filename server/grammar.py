import nltk

#paragraph = "The unicorn is a legendary animal that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian."
paragraph = "If it can't match the rest of the pattern, \{(12 backtracks,)] each time discarding one of the matches until it can either match the entire pattern or be certain that it cannot get a match."
#paragraph = "You can iterate pretty much anything in python using the for loop construct, for example, open('file.txt') returns a file object (and opens the file), iterating over it iterates over lines in that file \t for line in open(filename): # do something with line If that seems like magic, well it kinda is, but the idea behind it is really simple."

# GRAMMAR
# NP: noun phrase - contains a determinant or adjectives with nouns OR proper noun(s)
# NPX: list OR noun phrase involving participals used as adjectives
# VP: verb phrase - contains a determinant or adverbs with verbs
# VPX: deals with verb phrases such as "be certain" or "be sure"
# PRP: prepositional phrases, etc.
# OTH: deals with phrases that start with "or," "and," etc.
# see http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html and http://www.nltk.org/book/ch07.html for more information
grammar = r"""
    NP: {(<DT>|<PDT>)?(<CD>)?(<JJ>|<JJR>|<JJS>)*(<NN>|<NNS>|<NNP>|<NNPS>|<CD>|(<ORGANIZATION>|<PERSON>|<LOCATION>|<DATE>|<TIME>|<MONEY>|<PERCENT>|<FACILITY>|<GPE>))+<,>*}
        {(<DT>|<PDT>)+(<JJ>|<JJR>|<JJS>)+<,>*}
        {<PRP>}
    VP: {<MD>?(<DT>|<PDT>)?(<RB>|<RBR>|<RBS>)*(<MD><RB>)?(<VB>|<VBD>|<VBG>|<VBN>|<VBP>|<VBZ>)+<,>*}

    NPX: {<NP>*<,>+<VP>+(<,>|<NP>)*}
    VPX: {<VP>+(<JJ>|<JJR>|<JJS>)+}
    PRP: {(<CD>|<NP>)?<IN>+(<NP>|<VP>|<NPX>|<VPX>)+}
    OTH: {<CC>+(<PRP>|<NP>|<VP>|<NPX>|<VPX>)+}
    """

def parse(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(tagged)
    resultTree = nltk.RegexpParser(grammar).parse(entities)

    return resultTree

parse(paragraph).draw()
