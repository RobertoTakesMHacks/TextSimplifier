var isOn = [];

chrome.browserAction.onClicked.addListener(function(tab) {
    if (isOn[tab.id]) {
        chrome.browserAction.setIcon({tabId: tab.id, path: "action@2x.png"});
        isOn[tab.id] = false;
    } else {
        chrome.browserAction.setIcon({tabId: tab.id, path: { "19": "Logo.png", "38": "Logo.png" }});
        isOn[tab.id] = true;
    }
});


function getPageContents() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
            console.log();
        });
    });
}
