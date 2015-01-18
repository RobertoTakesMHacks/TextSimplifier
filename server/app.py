from flask import Flask, render_template, request, url_for
from replacecommonphrases import replace_common_phrases
app = Flask(__name__)

paragraph = "The unicorn is a legendary animal that has been described since antiquity as a beast with a large, pointed, spiraling horn projecting from its forehead. The unicorn was depicted in ancient seals of the Indus Valley Civilization and was mentioned by the ancient Greeks in accounts of natural history by various writers, including Ctesias, Strabo, Pliny the Younger, and Aelian."

@app.route('/', methods=['POST'])
def handle_data():
    text = request.data
    print text
    new_text = replace_common_phrases(text)
    print new_text
    return new_text

if __name__ == '__main__':
    app.run()
