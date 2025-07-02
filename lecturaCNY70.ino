/* Programacion de SEGUIDOR DE LINEA usando ARDUINO, CNY70, DRIVER L298N.
Realizado por:THE FENIX-EMIC TRON.*/
int infraPin1 = 10;    // pin del infrarrojos utilizado como entrada digital en el lado derecho(#1).
int infraPin2 = 11;    // pin del infrarrojos utilizado como entrada digital en el lado izquierdo(#2).
int valorInfra1 = 0;  // Valor inicial de la lectura digital del infrarrojo #1.
int valorInfra2 = 0;  // Valor inicial de la lectura digital del infrarrojo #2.

void setup() { 
  Serial.begin(9600); // Comenzamos comunicacion serial.
  pinMode(infraPin1, INPUT);     // Inicializa el pin 1 como entrada digital.
  pinMode(infraPin2, INPUT);     // Inicializa el pin 2 como entrada digital. 
} 

void loop() { 
  valorInfra1 = digitalRead(infraPin1);   // Lee el valor de la entrada 10, esto es, el valor que lee el infrarrojo #1.
  Serial.print("SENSOR1 ");         //Imprimimos el texto "SENSOR1 "
  Serial.println(valorInfra1);    //Imprimimos la lectura del infrarrojo #1.
  valorInfra2 = digitalRead(infraPin2);    // Lee el valor de la entrada 11, esto es, el valor que lee el infrarrojo #2.
  Serial.print("SENSOR2 ");       //Imprimimos el texto "SENSOR2 "
  Serial.println(valorInfra2);    //Imprimimos la lectura del infrarrojo #2.
  delay(1000);  // delay de 1segundo
}


