"use script"

websocket_namespace = {
    // https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket

    init(){

        console.log("websocket init program")

        const socket = new WebSocket("ws://localhost:8765");

        socket.onopen = ()=>console.log("websocket connexion open")
        socket.onclose = ()=>console.log("websocket connexion close")

        // Listen for messages
        socket.addEventListener("message", function (event) {
            console.log("Message from server ", event.data);
            try {
                const key_value = event.data.split("=")
                const key = key_value[0]
                const value = key_value[1]
                console.log("key :",key, "value ",value);
                switch (key){
                    case '1':
                        display_namespace.set_Temperature_1(value)
                        break
                    case '2':
                        display_namespace.set_Temperature_2(value)
                        break
                    case '3':
                        display_namespace.set_Temperature_3(value)
                        break
                    case '4':
                        display_namespace.set_Temperature_4(value)
                        break
                }
            } catch (error) {
                console.log("error during websocket data analysis",error)                
            }
        })         

    }


}