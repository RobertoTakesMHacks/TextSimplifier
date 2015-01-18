chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.type === "get") {
        var data = document.body.innerHTML;
        sendResponse(data);
    } else if (request.type === "set") {
        var data = request.data;
        var originalData = request.originalData;

        document.body.innerHTML = data;
        sendResponse({data: "success"});
    }
});
