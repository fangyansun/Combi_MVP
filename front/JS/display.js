"use script"

let display_namespace = {

    temperature_1 : null,
    temperature_2 : null,
    temperature_3 : null,
    temperature_4 : null,

    init(){
        console.log("hello from display_namespace")
        
        this.temperature_1 = document.getElementById("temperature_1")
        this.temperature_2 = document.getElementById("temperature_2")
        this.temperature_3 = document.getElementById("temperature_3")
        this.temperature_4 = document.getElementById("temperature_4")

        // check if they exist
        const display_list = [this.temperature_1, this.temperature_2, this.temperature_3, this.temperature_4]
        let counter = 0
        display_list.forEach(element => {
            if (element == null){
                console.log(`Warning, the ${counter} html element of display_list is null`)
            }
            counter ++
        })

    },    

    set_Temperature_1(temperature){
        this.temperature_1.innerHTML = temperature
    },

    set_Temperature_2(temperature){
        this.temperature_2.innerHTML = temperature
    },

    set_Temperature_3(temperature){
        this.temperature_3.innerHTML = temperature
    },

    set_Temperature_4(temperature){
        this.temperature_4.innerHTML = temperature
    },

}