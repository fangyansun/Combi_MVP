void setup() {
  // put your setup code here, to run once:
  // choose the baudrate
  Serial.begin(9600);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  Serial.println("temp_1=45"); // send some info to the computer through USB
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  Serial.println("temp_2=90"); // send some info to the computer through USB
  delay(1000);                       // wait for a second 
}


// void setup() {
//     Serial.begin(9600); // Ouvre la communication série à 9600 bauds
// }

// void loop() {
//     int sensorValue = analogRead(A0); // Lire un capteur sur A0 (exemple)
//     float data = sensorValue * (5.0 / 1023.0); // Convertir en tension

//     Serial.print("Temp_car: ");
//     Serial.println(data);

//     Serial.print("Temp_ext: ");
//     Serial.println(data);

//     Serial.print("Temp_water: ");
//     Serial.println(data);    

//     Serial.print("Temp_motor: ");
//     Serial.println(data);

//     Serial.print("Speed: ");
//     Serial.println(data);

//     Serial.print("GPS1: ");
//     Serial.println(data);

//     Serial.print("GPS2: ");
//     Serial.println(data);

//     delay(1000); // Attendre 1 seconde
// }
