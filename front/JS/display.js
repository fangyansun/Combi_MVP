"use script"

let display_namespace = {

    speed : null,
    temperature_car : null,
    temperature_motor : null,
    temperature_water : null,
    temperature_ext : null,

    init(){
        
        this.speed         = document.getElementById("speed")
        this.temperature_car = document.getElementById("temperature_car")
        this.temperature_motor = document.getElementById("temperature_motor")
        this.temperature_water = document.getElementById("temperature_water")
        this.temperature_ext = document.getElementById("temperature_ext")

        // check if they exist
        const display_list = [this.speed, this.temperature_car, this.temperature_motor, this.temperature_water, this.temperature_ext]
        let counter = 1
        display_list.forEach(element => {
            if (element == null){
                console.log(`Warning, the ${counter} html element of display_list is null`)
            }
            counter ++
        })

    },

    set_Speed(speed){
        this.speed.innerHTML = speed
    },

    set_Temperature_car(temperature){
        this.temperature_car.innerHTML = temperature
    },

    set_Temperature_motor(temperature){
        this.temperature_motor.innerHTML = temperature
    },

    set_Temperature_water(temperature){
        this.temperature_water.innerHTML = temperature
    },

    set_Temperature_ext(temperature){
        this.temperature_ext.innerHTML = temperature
    },

}