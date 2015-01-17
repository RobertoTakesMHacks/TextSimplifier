chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.type == "get") {
        sendResponse({"data": document.body.innerHTML});
    } else if (request.type == "set") {
        document.body.innerHTML = request.data;
        sendResponse({"success": true});
    }
});
