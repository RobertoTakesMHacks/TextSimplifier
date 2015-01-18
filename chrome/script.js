chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.type == "get") {
        sendResponse({"data": document.body.innerHTML});
    } else if (request.type == "set") {
        var data = request.data;
        var originalData = request.originalData;

        appendToPage(data, originalData);
        sendResponse({"success": true});
    }
});

function wordCount(text) {
    return text.split(/[^a-z0-9]+/i).length || 1;
}

function sentenceCount(text) {
    return text.replace(/[^\.!?]/g, '').length || 1;
}

var function averageSyllablesPerWord(text, wordCount) {
    var syllableCount = 0;

    text.split(/\s+/).forEach(function(word) {
        syllableCount += syllableCount(word);
    });

    // Prevent NaN...
    return (syllableCount||1) / (wordCount||1);
}

function syllableCount(text) {
    var syllableCount = 0,
    prefixSuffixCount = 0,
    wordPartCount = 0;

    // Prepare word - make lower case and remove non-word characters
    word = word.toLowerCase().replace(/[^a-z]/g,"");

    // Specific common exceptions that don't follow the rule set below are handled individually
    // Array of problem words (with word as key, syllable count as value)
    var problemWords = {
        "simile":		3,
        "forever":		3,
        "shoreline":	2
    };

    // Return if we've hit one of those...
    if (problemWords.hasOwnProperty(word)) return problemWords[word];

    // These syllables would be counted as two but should be one
    var subSyllables = [
    /cial/,
    /tia/,
    /cius/,
    /cious/,
    /giu/,
    /ion/,
    /iou/,
    /sia$/,
    /[^aeiuoyt]{2,}ed$/,
    /.ely$/,
    /[cg]h?e[rsd]?$/,
    /rved?$/,
    /[aeiouy][dt]es?$/,
    /[aeiouy][^aeiouydt]e[rsd]?$/,
    /^[dr]e[aeiou][^aeiou]+$/, // Sorts out deal, deign etc
    /[aeiouy]rse$/ // Purse, hearse
    ];

    // These syllables would be counted as one but should be two
    var addSyllables = [
    /ia/,
    /riet/,
    /dien/,
    /iu/,
    /io/,
    /ii/,
    /[aeiouym]bl$/,
    /[aeiou]{3}/,
    /^mc/,
    /ism$/,
    /([^aeiouy])\1l$/,
    /[^l]lien/,
    /^coa[dglx]./,
    /[^gq]ua[^auieo]/,
    /dnt$/,
    /uity$/,
    /ie(r|st)$/
    ];

    // Single syllable prefixes and suffixes
    var prefixSuffix = [
    /^un/,
    /^fore/,
    /ly$/,
    /less$/,
    /ful$/,
    /ers?$/,
    /ings?$/
    ];

    // Remove prefixes and suffixes and count how many were taken
    prefixSuffix.forEach(function(regex) {
        if (word.match(regex)) {
            word = word.replace(regex,"");
            prefixSuffixCount ++;
        }
    });

    wordPartCount = word
    .split(/[^aeiouy]+/ig)
    .filter(function(wordPart) {
        return !!wordPart.replace(/\s+/ig,"").length
    })
    .length;

    // Get preliminary syllable count...
    syllableCount = wordPartCount + prefixSuffixCount;

    // Some syllables do not follow normal rules - check for them
    subSyllables.forEach(function(syllable) {
        if (word.match(syllable)) syllableCount --;
    });

    addSyllables.forEach(function(syllable) {
        if (word.match(syllable)) syllableCount ++;
    });

    return syllableCount || 1;
}

function fleschScore(text) {
    var numberOfSentences = sentenceCount(text);
    var numberOfWords = wordCount(text);
    var averageNumberOfSyllables = averageSyllablesPerWord(text, numberOfWords);

    return 206.835 - 1.015 * (numberOfWords/numberOfSentences) - 84.6 * (averageNumberOfSyllables);
}

function appendToPage(data, originalData) {
    var fleschScore = fleschScore(data);
    var originalFleschScore = fleschScore(originalData);

    var htmlToAppend = "
        <script type='text/javscript'>
            #simplified-document {
                position: absolute;
                left: 0;
                right: 0;
                top: 0;
                bottom: 0;
                z-index: 90000;
                background-color: rgba(0, 0, 0, 0.7);
            }
            #simplified-wrapper {
                z-index: 100000;
                width: " + Math.floor($(document.window).width() / 2) + " px;
                min-width: 650px;
                min-height: 100px;
                background-color: white;
                color: black;

                padding: 30px;
                left: auto;
                right: auto;
            }
            #flesh-score {
                text-align: center;
            }
            #simplified-text {
                text-align: right;
            }
        </script>

        <div id='simplified-document'>
            <div id='simplified-wrapper'>
                <div id='flesch-score'>
                    Flesch-Kincaid Score: " + fleschScore + ". Original: " + originalFleschScore + "
                </div>

                <div id='simplified-text'>
                " + data + "
                </div>
            </div>
        </div>";

    document.body.innerHTML += htmlToAppend;
}
