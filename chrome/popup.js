chrome.tabs.executeScript( {
    code: 'window.getSelection().toString();'
}, function(selection) {
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
