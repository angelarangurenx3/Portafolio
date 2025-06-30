int led=6;
int cny=7;
int valorCNY=0; //informacion recibida del sensor
void setup() {
  pinMode(led,OUTPUT); //la variable led solo se enciende o se apaga
  pinMode(cny,INPUT); //la variable cny solo recibe señales
}

void loop() {
  valorCNY=digitalRead(cny); // se guardan los datos recibidos de la variable cny asociada con el pin 7
  digitalWrite(led,valorCNY); //los valores tomados por la variable valorCNY seran enviados a la variable led
}
