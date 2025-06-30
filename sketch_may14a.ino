int TRIG = 10;
int ECO = 9;
int LED = 3;
int DURACION;
int DISTANCIA;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECO, INPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600); //9600 es la taza de velocidad de comunicacion para plasmar en monitor serial
}

void loop() {
  digitalWrite(TRIG, HIGH); //trigger envia una señal
  delay(1);
  digitalWrite(TRIG, LOW); //trigger deja de enviar la señal
  DURACION = pulseIn(ECO, HIGH); //tiempo que tarda en responder mediante el pin ECO
  DISTANCIA = DURACION / 58.2; //con esto se obtiene la distancia medida en cm
  Serial.println(DISTANCIA); //println significa print line
  delay(200);
}
