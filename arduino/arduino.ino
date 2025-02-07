void setup() {
  // put your setup code here, to run once:
  // choose the baudrate
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {  
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    
    int sensorValue = analogRead(A0); // Lire un capteur sur A0 (exemple)
    float data = sensorValue * (5.0 / 1023.0); // Convertir en tension

    Serial.print("Temp_car=");
    Serial.println(data);

    Serial.print("Temp_ext=");
    Serial.println(data++);

    Serial.print("Temp_water=");
    Serial.println(data++);    

    Serial.print("Temp_motor=");
    Serial.println(data++);

    Serial.print("Speed=");
    Serial.println(data++);

    Serial.print("GPS1=");
    Serial.println(data++);

    Serial.print("GPS2=");
    Serial.println(data);

    delay(500); // Attendre 1/2 secondes
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(500); // Attendre 1/2 secondes    
}

