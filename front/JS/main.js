"use script"

let main_namespace = {

    temperature_1 : document.getElementById("temperature_1"),
    temperature_2 : document.getElementById("temperature_2"),
    temperature_3 : document.getElementById("temperature_3"),
    temperature_4 : document.getElementById("temperature_4"),

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

console.log("hello")
main_namespace.set_Temperature_1(50)



