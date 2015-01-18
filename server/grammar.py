import nltk

#paragraph = "The unicorn is a legendary animal that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian."
#paragraph = "If it can't match the rest of the pattern, \{(12 backtracks,)] each time discarding one of the matches until it can either match the entire pattern or be certain that it cannot get a match."
#paragraph = "You can iterate pretty much anything in python using the for loop construct, for example, open('file.txt') returns a file object (and opens the file), iterating over it iterates over lines in that file \t for line in open(filename): # do something with line If that seems like magic, well it kinda is, but the idea behind it is really simple."
#paragraph = "Greenland is the world's largest island with an area of over 2.1 million km squared, while Australia, the world's smallest continent has an area of 7.6 million km squared, but there is no standard of size which distinguishes islands from continents, or from islets."
#paragraph = "The socio-economic diversity of these regions ranges from the Stone Age societies in the interior of Madagascar, Borneo or Papua New Guinea to the high-tech lifestyles of the city-islands of Singapore and Hong Kong."
paragraph = "Anna Laura loves Moby very much. She especially likes when he breathes under the covers and smiles."

# GRAMMAR
# S: Symbol or punctuation
# NE: Named entities
# NP: noun phrase - contains a determinant or adjectives with nouns OR proper noun(s)
# NPX: list OR noun phrase involving participals used as adjectives
# VP: verb phrase - contains a determinant or adverbs with verbs
# VPX: deals with verb phrases such as "be certain" or "be sure"
# see http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html and http://www.nltk.org/_modules/nltk/tag/stanford.html#POSTagger for more information

# VPX: {(<MD><RB>)?(<VP>)+}
# |(<ORGANIZATION>|<PERSON>|<LOCATION>|<DATE>|<TIME>|<MONEY>|<PERCENT>|<FACILITY>|<GPE>))+
grammar = r"""
    S: {<,>|<.>}
    NE: {<ORGANIZATION>|<PERSON>|<LOCATION>|<DATE>|<TIME>|<MONEY>|<PERCENT>|<FACILITY>|<GPE>}
    NP: {(<DT>|<PDT>)?<IN>*<CC>?(<DT>|<PDT>)?<PRP\$>*<CD>*(<RB>|<RBR>|<RBS>|<VBG>)*(<JJ>|<JJR>|<JJS>|<VBG>)*<S>*(<JJ>|<JJR>|<JJS>|<VBG>)*<S>*(<JJ>|<JJR>|<JJS>|<VBG>)*<S>*(<NN>|<NNS>|<NNP>|<NNPS>|<NE>)+}
        {<IN>?<PRP>+}
        {<CD>?(<NN>|<NNS>|<NNP>|<NNPS>|<NE>)*}
    VP: {<MD>?<WDT>?(<JJ>|<JJR>|<JJS>|<VBG>)*(<RB>|<RBR>|<RBS>)*<PRP\$>*(<VB>|<VBD>|<VBG>|<VBN>|<VBP>|<VBZ>)+(<JJ>|<JJR>|<JJS>|<VBG>)*<IN>?}
    """

def parse(text):
    #tokenize words
    tokens = nltk.word_tokenize(text)
    # tagged = nltk.pos_tag(tokens)
    #create Stanford tagger
    st = nltk.tag.stanford.POSTagger('english-bidirectional-distsim.tagger', 'stanford-postagger.jar')
    #create list of tagged words
    tagged = st.tag(tokens)
    entities = nltk.ne_chunk(tagged)
    resultTree = nltk.RegexpParser(grammar).parse(entities)
    #r = resultTree.get_descendants()
    #print r

    return resultTree

parse(paragraph).draw()

def correct():
    chunks = list(self._paragraph)
    return [c[1] for c in chunks]
