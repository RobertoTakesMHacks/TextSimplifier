var isOn = [];

chrome.browserAction.onClicked.addListener(function(tab) {
    if (isOn[tab.id]) {
        chrome.browserAction.setIcon({tabId: tab.id, path: {"19": "off.png", "38": "off@2x.png"} });
        isOn[tab.id] = false;
        //refreshes the page
        chrome.tabs.getSelected(null, function(tab) {
            var code = 'window.location.reload();';
            chrome.tabs.executeScript(tab.id, {code: code});
        });
    } else {
        chrome.browserAction.setIcon({tabId: tab.id, path: {"19": "on.png", "38": "on@2x.png"} });
        isOn[tab.id] = true;
        //get page contents
        getPageContents(function(res) {
            console.log(res.data);
        })
    }
});


function getPageContents(cb) {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {data: "getPageContents"}, function(response) {
            cb(response);
        });
    });
}
