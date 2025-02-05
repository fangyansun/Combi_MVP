"use script"

websocket_namespace = {
    // https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket

    init(){

        console.log("websocket init program")

        // Create WebSocket connection.
        const socket = new WebSocket("ws://localhost:8765");

        // Connection opened
        socket.addEventListener("open", function (event) {
            socket.send("Hello Server!");
        });

        // Listen for messages
        socket.addEventListener("message", function (event) {
            console.log("Message from server ", event.data);
        });

    }


}


websocket_namespace.init()

console.log("hello from websocket")