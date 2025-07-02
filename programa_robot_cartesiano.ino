int x;
int y;
int MOTOR_IZQUIERDO = 3;
int MOTOR_DERECHO = 5;
int MOTOR_ABAJO = 6;
int LDR = 8;
int MOTOR_ARRIBA = 9;
int SONIDO = 2;
int ECO = 13;
int d;
int t;

void setup() {
  // put your setup code here, to run once:
  pinMode(MOTOR_IZQUIERDO, OUTPUT);
  pinMode(MOTOR_DERECHO, OUTPUT);
  pinMode(MOTOR_ABAJO, OUTPUT);
  pinMode(MOTOR_ARRIBA, OUTPUT);
  pinMode(SONIDO, OUTPUT);
  pinMode(ECO, INPUT);
  pinMode(4, OUTPUT);
  digitalWrite(SONIDO, LOW);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
{
  x=analogRead(A0);
  y=analogRead(A1);
  int LRD = analogRead(A2);
  Serial.println(LDR);
  digitalWrite(SONIDO, HIGH);
  delayMicroseconds(10);
  digitalWrite(SONIDO, LOW);
    t=pulseIn(ECO, HIGH);
    d=t/59;

if(x >= 0 && x < 480){
  analogWrite(MOTOR_IZQUIERDO, map(x, 0, 480, 255, 0));
  }else{
  analogWrite(MOTOR_IZQUIERDO, 0);
}
if(x > 520 && x <= 1023){
  analogWrite(MOTOR_DERECHO, map(x, 520, 1023, 0, 255));
  }else{
  analogWrite(MOTOR_DERECHO, 0);
  }
if(y >= 0 && y < 480){
  analogWrite(MOTOR_ABAJO, map(y, 0, 480, 255, 0));
  }else{
  analogWrite(MOTOR_ABAJO, 0);
  }
if(y > 520 && y <= 1023){
  analogWrite(MOTOR_ARRIBA, map(y, 520, 1023, 0, 255));
  }else{
  analogWrite(MOTOR_ARRIBA, 0);
  }
if(LDR > 500)
{
  digitalWrite(4,HIGH);
  }
  else
  {
  digitalWrite(4,LOW);
  }
if(d>=10)
{
  digitalWrite(MOTOR_IZQUIERDO, HIGH);
  digitalWrite(MOTOR_DERECHO, LOW);
  digitalWrite(MOTOR_ABAJO, LOW);
  digitalWrite(MOTOR_ARRIBA, LOW);
}
if(d<=9)
{
  digitalWrite(MOTOR_IZQUIERDO, LOW);
  digitalWrite(MOTOR_DERECHO, LOW);
  digitalWrite(MOTOR_ABAJO, LOW);
  digitalWrite(MOTOR_ARRIBA, LOW);
  delay(5000);
}
}
}
