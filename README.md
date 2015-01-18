# Text Simplifier
MHacks V 2015

##Concept
This Text Simplifier is a beta version of a larger idea. The idea is simple: to help improve the global literacy rates. But it is hard to implement. Half of children not attending school come from conflict-afflicted areas. So the problem becomes not to bring them to education, but bring the education to them. The obstacle is the lack of stability and access to resources. Textbooks and internet dependent programs can be pricey and impossible.

Our idea is a tool that simplifies text. The essential concept is that a child, teen, or adult can type in a subject, chose a level, and have access to an article on their level to read. Then once they understand, they can choose a harder level. The program could be universal and distributed on tablets to households.

Since MHacks V is just 36 hours, what we have created is a beta version that uses the internet. Our text simplifier is a Chrome extension that edits a page and makes it easier to read by grade level. There is currently only one setting, and since our team is very new to natural language processing, it's not an incredibly drastic change. But it works.

##How it works
The way this currently works is by using a list of english words ordered by frequency of use. Whenever it encounters a word that is not of a specific frequency or better, it replaces that word with the best fit synonym. If it cannot find a synonym that is a better fit, and it is an adjective or an adverb, it removes the word entirely since in many cases, sentences will keep their meaning regardless of these types of words.

This tool also has a method for finding the logical structure of a body of text using a tree and identifying prepositional phrases or sections of other patterns. This way, in the future, we can find logical chunks that can be removed or reworded for a much more flawproof way of simplifying. The problem now is efficiency, as navigating and manipulating the tree can be very slow.

##Installation
* Clone this repository
* Go to [chrome://extensions](chrome://extensions) in Google Chrome
* Check "Developer mode" in the upper right and then click "Load unpacked extension" in the upper left
* Navigate to the [chrome](/chrome) folder of this repository then click "Select" in the popup window
* Follow the steps [here](http://www.nltk.org/install.html) for installing NLTK, a python library we make heavy use of
* Follow the steps [here](http://www.nltk.org/data.html) for installing the NLTK data. We selected the "all" option described there
* Make sure [pip](https://pypi.python.org/pypi/pip) is installed on your machine
* Go to the [server](/server) folder in the terminal
* Run `pip install flask` and `pip install beautifulsoup4`. If either doesn't work, add `sudo` to the beginning of the command

##Running
* In the terminal, navigate to the [server](/server) folder of this repository
* Run `python app.py`
* In Chrome, go to a page you want to simplify. We have tested primarily with Wikipedia pages
* Click the extension icon and wait a little bit after it's highlighted for the page text to be replaced by simpler text
* You can compare the readability of the two blocks of text returned (our simplified version and the original version) at [Readability-Score.com](https://readability-score.com/)
