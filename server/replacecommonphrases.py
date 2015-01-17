import json
import nltk

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
for key in common_phrases_keys :
    if key in paragraph:
        print 'key is in paragraph'
        print key
        print common_phrases[key]
        paragraph = paragraph.replace(key, common_phrases[key])


porterStemmer = nltk.stem.porter.PorterStemmer()
words = paragraph.split(' ')
for word in words:
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.lower()
    stemmed = porterStemmer.stem(word)
    if stemmed in common_stem_words:
        print word
    else:
        print word + ' is not common!'

print paragraph
