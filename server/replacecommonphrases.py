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

def replace_phrases(text):
    print 'replacing phrases'
    newText = text
    for key in common_phrases_keys :
        if key in newText:
            newText = newText.replace(key, common_phrases[key])
    return newText


def replace_uncommon_words(text):
    print 'replacing uncommon words'
    newText = ''
    porterStemmer = nltk.stem.porter.PorterStemmer()
    words = text.split(' ')
    for word in words:
        punc = ''
        istitle = False
        if '.' in word:
            punc = '.'
            word = word.replace('.', '')
        elif ',' in word:
            punc = ','
            word = word.replace(',', '')
        if word.istitle():
            istitle = True
            word = word.lower()
        stemmed = porterStemmer.stem(word)
        if stemmed in common_stem_words:
            if istitle:
                word = word.title()
            newText += word + punc + ' '
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
                stemmed_syn = porterStemmer.stem(synonym)
                if stemmed_syn in common_stem_words:
                    index = common_stem_words.index(stemmed_syn)
                    if index < how_common:
                        how_common = index
                        word_to_use = synonym
            if word_to_use == word and removable:
                print 'removing ' + word
            else:
                if istitle:
                    word_to_use = word_to_use.title()
                newText += word_to_use + punc + ' '
    return newText

#TODO if there is a list of three or more items (eg. something, something else, and something else)
# replace it with

def replace_common_phrases(text):
    new_text = replace_phrases(text)
    new_text = replace_uncommon_words(text)
    return new_text
