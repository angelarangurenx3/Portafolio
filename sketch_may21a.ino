int IN1 = 8;
int IN2 = 9;
int IN3 = 10;
int IN4 = 11;
int demora = 20;//demora entre pasos, no debe ser menor a 10 ms. Como no existe pin 20 en el arduino, por default el arduino toma el valor como tiempo de espera en ms

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}

void loop() {
  for (int i = 0; i < 512; i++)// como el motor solo tiene 4 posiciones y requiere 2048 pasos para hacer una revolucion 2048/4 = 512
  {
    digitalWrite(IN1,HIGH);   //paso 1
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
    delay(demora);

    digitalWrite(IN1,LOW);   //paso 2
    digitalWrite(IN2,HIGH);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,LOW);
    delay(demora);

    digitalWrite(IN1,LOW);   //paso 3
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
    delay(demora);

    digitalWrite(IN1,LOW);   //paso 4
    digitalWrite(IN2,LOW);
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    delay(demora);
  }
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
  delay(5000);              //el motor se detiene por 5 segundos.
}
