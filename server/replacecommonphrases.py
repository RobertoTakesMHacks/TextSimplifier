import json
import nltk
from nltk.corpus import wordnet as wn
import grammar
import re

common_phrases_keys_json = open('words/commonphraseskeys.json')
common_phrases_json = open('words/commonphrases.json')
common_stem_words_json = open('words/commonstemwords.json')

common_phrases_keys = json.load(common_phrases_keys_json)
common_phrases = json.load(common_phrases_json)
common_stem_words = json.load(common_stem_words_json)
common_phrases_keys_json.close()
common_phrases_json.close()
common_stem_words_json.close()

# bad practice. I don't care anymore
prepositionList = ["aboard","about","above","across","after","against","along","amid","among","anti","around","as","at","before","behind","below","beneath","beside","besides","between","beyond","but","by",
"concerning","considering","despite","down","during","except","excepting","excluding","following","for","from","in","inside","into","like","minus","near","of","off","on","onto","opposite","outside","over","past",
"per","plus","regarding","since","than","through","toward","towards","under","underneath","unlike","until","up","upon","versus","via","with","within","without"]


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

def replace_complex_sections(text):
    parsed = grammar.parse(text) # result is a treebank
    return navigate(parsed)

def navigate(treebank): #result is a string
    result_tree = nltk.tree.Tree("S", [])

    for child in treebank:

        i = 3
        if str(child)[:3] == "(NP":
            while (str(child)[i] == " ") or (str(child)[i] == "\n") or (str(child)[i:(i+8)] == "(S ,/,)"):
                if (str(child)[i:(i+8)] == "(S ,/,)"):
                    i += 8
                else:
                    i += 1

            for preposition in prepositionList:
                shouldContinue = False
                if (preposition + "/") in str(child)[i:(i+15)]:
                    shouldContinue = True
                    break

            if shouldContinue:
                continue

        result_tree.append(child) # result is a treebank

    for subtree in result_tree.subtrees():
        #print dir(subtree) # tells you properties on object
        pass

    words = result_tree.pos() # sequence of unicode words
    result_words = ""
    for token in words:
        result_words += token[0][0] + " "
        
    result_words = re.sub(r' (\W|\D) ', r'\1 ', result_words)

    result = result_words.encode('latin_1')
    return result

print replace_complex_sections("The unicorn is a legendary animal that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian.")

def replace_common_phrases(text):
    new_text = replace_phrases(text)
    new_text = replace_uncommon_words(text)
    return new_text
