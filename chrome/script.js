chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.type === "get") {
        var data = document.body.innerHTML;
        sendResponse(data);
    } else if (request.type === "set") {
        var data = request.data;

        sendResponse({data: "success"});

        document.body.innerHTML = data;
    }
});
