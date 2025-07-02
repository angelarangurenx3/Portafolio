
int infraPin1 = 10;
int infraPin2 = 11;
int valorInfra1 = 0;
int valorInfra2 = 0;
int OUTPUT4 = 4;
int OUTPUT3 = 3;
int OUTPUT2 = 6;
int OUTPUT1 = 7;
void setup() { 
  Serial.begin(9600);
  pinMode(infraPin1, INPUT);
  pinMode(infraPin2, INPUT);
  pinMode (OUTPUT1, OUTPUT);
  pinMode (OUTPUT2, OUTPUT);
  pinMode (OUTPUT3, OUTPUT);
  pinMode (OUTPUT4, OUTPUT);
  } 
void loop() { 
  valorInfra1 = digitalRead(infraPin1);
  Serial.print("SENSOR1 ");
  Serial.println(valorInfra1);
  valorInfra2 = digitalRead(infraPin2);
  Serial.print("SENSOR2 ");
  Serial.println(valorInfra2);
  if(valorInfra1==0)
  {
  if(valorInfra2==0)
  {
  digitalWrite(OUTPUT1,0);
  digitalWrite(OUTPUT2,1);
  digitalWrite(OUTPUT3,1);
  digitalWrite(OUTPUT4,0); 
  }
  else
  {
  digitalWrite(OUTPUT1,0);
  digitalWrite(OUTPUT2,0);
  digitalWrite(OUTPUT3,1);
  digitalWrite(OUTPUT4,0); 
  }
  }
  else 
  {if(valorInfra2==0) 
  {
  digitalWrite(OUTPUT3,0);
  digitalWrite(OUTPUT4,0);
  digitalWrite(OUTPUT1,0);
  digitalWrite(OUTPUT2,1);
  }
  else{ 
  digitalWrite(OUTPUT1,1);
  digitalWrite(OUTPUT2,0);
  digitalWrite(OUTPUT3,0);
  digitalWrite(OUTPUT4,1);
  } 
  }
  }
