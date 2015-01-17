// importing word files
var commonPhrases;
var commonPhrasesKeys;
var commonStemWords;
var commonWords;

walk(document.body);

function walk(node) {
    var child, next;

    switch ( node.nodeType ) {
        case 1:
        case 9:
        case 11:
        child = node.firstChild;
        while ( child ) {
            next = child.nextSibling;
            walk(child);
            child = next;
        }
        break;

        case 3:
        handleText(node);
        break;
    }
}

function handleText(textNode) {
    var t = textNode.nodeValue;

    t.replace(/clouds/g, "butts");

    textNode.nodeValue = t;
}




/*chrome.tabs.executeScript( {
    code: 'window.getSelection().toString();'
}, function(selection) {

    parseSelection(selection, function(selection) {


        //outputting result.
        document.getElementById("status").textContent = selection;

        var x = new XMLHttpRequest();
        x.open('POST', 'http://localhost:3000', true);
        x.responseType = 'text';
        x.onload = function() {
            var response = x.response;
            if (!response) {
                errorCallback('No response from server!');
                return;
            }
            x.onerror = function() {
                errorCallback('Network error.');
            };
        }
        x.send('text=' + selection);
    });
});*/


function parseSelection(selection, cb) {
    var keys = Object.keys(phrases);
    selection = String(selection); //DO NOT ASK WHY.

    for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var phrase = phrases[key];
        var re = new RegExp(key, "g");

        selection.replace(re, phrase);
    }

    cb(selection);
}
