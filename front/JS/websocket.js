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
                switch (key){
                    case 'Temp_car':
                        display_namespace.set_Temperature_1((1*value).toFixed(1))
                        break
                    case 'Temp_motor':
                        display_namespace.set_Temperature_2((10*value).toFixed(1))
                        break
                    case 'Temp_water':
                        display_namespace.set_Temperature_3((5*value).toFixed(1))
                        break
                    case 'Temp_ext':
                        display_namespace.set_Temperature_4((value-4).toFixed(1))
                        break
                    case 'Speed':
                        display_namespace.set_Speed((50*value).toFixed(1))
                        break
                    case 'GPS_1':
                        // TODO
                        break
                    case 'GPS_2':
                        // TODO
                        break
                    default:
                        console.log("we received a message with an unknown key : ", key)
                }
            } catch (error) {
                console.log("error during websocket data analysis",error)                
            }
        })         

    }


}