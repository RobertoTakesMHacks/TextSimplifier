import json
import nltk
from nltk.corpus import wordnet as wn

common_phrases_keys_json = open('words/commonphraseskeys.json')
common_phrases_json = open('words/commonphrases.json')
common_stem_words_json = open('words/commonstemwords.json')

common_phrases_keys = json.load(common_phrases_keys_json)
common_phrases = json.load(common_phrases_json)
common_stem_words = json.load(common_stem_words_json)
common_phrases_keys_json.close()
common_phrases_json.close()
common_stem_words_json.close()

paragraph = "The unicorn is a legendary animal that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian."
def replace_phrases(text):
    newText = text
    for key in common_phrases_keys :
        if key in newText:
            newText = newText.replace(key, common_phrases[key])
    return newText


def replace_uncommon_words(text): #FIXME DOWNCASES AND REMOVES PUNCTUATION
    newText = ''
    porterStemmer = nltk.stem.porter.PorterStemmer()
    words = text.split(' ')
    for word in words:
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.lower()
        stemmed = porterStemmer.stem(word)
        if stemmed in common_stem_words:
            newText += word + ' '
        else:
            synsets = wn.synsets(word)
            word_to_use = word
            how_common = 20000
            removable = False
            for synset in synsets:
                split_synset = synset.name().split('.')
                synonym = split_synset[0]
                pos = split_synset[1]
                if pos == 's' or pos == 'r' or pos == 'a':
                    removable = True
                print synonym
                print pos
                stemmed_syn = porterStemmer.stem(synonym)
                if stemmed_syn in common_stem_words:
                    index = common_stem_words.index(stemmed_syn)
                    if index < how_common:
                        how_common = index
                        word_to_use = synonym
            if word_to_use == word and removable:
                print 'removing ' + word
            else:
                newText += word_to_use + ' '
    return newText


print replace_uncommon_words(paragraph)
print paragraph
