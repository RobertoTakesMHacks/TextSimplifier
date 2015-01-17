from flask import Flask, render_template, request, url_for
import nltk
app = Flask(__name__)

porterStemmer = nltk.stem.porter.PorterStemmer()
# print porterStemmer.stem('someword')
wn = nltk.corpus.wordnet

@app.route('/', methods=['POST'])
def handle_data():
    print request.form;
    return 'New Text'

if __name__ == '__main__':
    app.run()

def replace_uncommon_words(text):
    print 'replacing difficult words'

    return text;

def replace_common_phrases(text):
    print 'replacing common phrases'
    return text
