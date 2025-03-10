"use script"

websocket_namespace = {
    // https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket

    init(){

        console.log("websocket init program")

        //const socket = new WebSocket("ws://192.168.3.2:8765");
        
        let socket = new WebSocket("ws://192.168.137.1:8765");

        socket.onopen = ()=>{
            console.log("websocket connexion open")            
        }
        socket.onclose = ()=>{
            console.log("websocket connexion close, we will relaunch the websocket init program")
            this.init()
        }

        // Listen for messages
        socket.addEventListener("message", function (event) {
            // console.log("Message from server ", event.data);
            try {
                const key_value = event.data.split("=")
                const key = key_value[0]
                const value = key_value[1]
                switch (key){
                    case 'Temp_car':
                        display_namespace.set_Temperature_car(      parseFloat(value).toFixed(1))
                        break
                    case 'Temp_motor':
                        display_namespace.set_Temperature_motor(    parseFloat(value).toFixed(1))
                        break
                    case 'Temp_water':
                        display_namespace.set_Temperature_water(    parseFloat(value).toFixed(1))
                        break
                    case 'Temp_ext':
                        display_namespace.set_Temperature_ext(      parseFloat(value).toFixed(1))
                        break
                    case 'Speed':
                        display_namespace.set_Speed(                parseFloat(value).toFixed(1))
                        break
                    case 'GPS1':
                        // TODO
                        break
                    case 'GPS2':
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