int LED = 3;
int BRILLO;
int POT = 0; //potenciometro ubicado en la entrada A0 de la seccion analogica

void setup() {
  pinMode(LED, OUTPUT);
  //las entradas analogicas no requieren inicializacion
}

void loop() {
  BRILLO = analogRead(POT) / 4;
  //el valor de intensidad de la variable BRILLO está sujeta al valor de la variable POT
  //la division entre 4 es porque analogRead utiliza valores que van de 0 a 1023
  //de esta manera la variable BRILLO tomará valores utiles para analogWrite
  analogWrite(LED, BRILLO);
  //con este comando se escribirá el valor leido en LED
  //funciona con valores que van de 0 a 255
  //con la division de analogRead, los valores READ-WRITE encajan
}
