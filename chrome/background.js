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
            sendContentsToServer(res.data);
        })
    }
});


function getPageContents(cb) {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {data: "getPageContents"}, function(response) {
            console.log(response);

            cb(response);
        });
    });
}

function sendContentsToServer(data) {
    vaar xmlhttp = null;

    function processRequest() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            if (xmlHttp.responseText == "Not found") {
                alert("Oops. No server found.");
            } else {
                console.log(xmlhttp.responseText);
            }
        }
    }

    xmlHttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = processRequest;
    xmlHttp.open("POST", "http://localhost:5000", false);
    xmlHttp.send({ "html": data });
    return xmlHttp.responseText;
}
