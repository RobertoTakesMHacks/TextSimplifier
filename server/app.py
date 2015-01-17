import nltk

paragraph = "The unicorn is a legendary animal that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian."

grammar = r"""
    NP: {<DT>?<JJ>*<NN>}
        {<NNP>+}
    """

def parse(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(tagged)
    resultTree = nltk.RegexpParser(grammar).parse(entities)

    return resultTree

parse(paragraph).draw()
