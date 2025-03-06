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
    Serial.println(11);

    Serial.print("Temp_water=");
    Serial.println(22);    

    Serial.print("Temp_motor=");
    Serial.println(33);

    Serial.print("Speed=");
    Serial.println(44);

    Serial.print("GPS1=");
    Serial.println(55);

    Serial.print("GPS2=");
    Serial.println(66);

    delay(600); // Attendre 600 ms
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(600); // Attendre 600 ms
}
