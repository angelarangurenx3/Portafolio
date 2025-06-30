int x; //se almacena el valor leido de la entrada analogica correspondiente al eje x
int y; //se almacena el valor leido de la entrada analogica correspondiente al eje y
int SW; //se almacena el valor leido de la entrada analogica correspondiente al pulsador
int LED_IZQUIERDA = 3;
int LED_DERECHA = 5;
int LED_ABAJO = 6;
int LED_ARRIBA = 9;
int PULSADOR = 10;
int LED_SW = 11;

void setup(){
  pinMode(LED_IZQUIERDA, OUTPUT);
  pinMode(LED_DERECHA, OUTPUT);
  pinMode(LED_ABAJO, OUTPUT);
  pinMode(LED_ARRIBA, OUTPUT);
  pinMode(LED_SW, OUTPUT);
  pinMode(PULSADOR, INPUT);
  //entradas analogicas no requieren inicializacion
}

void loop(){
  x = analogRead(A0); //se realiza una lectura analogica del valor del potenciometro del eje 'x' y se dirige al pin A0
  y = analogRead(A1); //se realiza una lectura analogica del valor del potenciometro del eje 'y' y se dirige al pin A1
  SW = digitalRead(PULSADOR); //se realiza una lectura digital del valor del switch (0 o 1) y se dirige al pin relacionado con la variable PULSADOR
  if (x >=0 && x <480){       //el && significa que ambas condiciones deben ser ciertas
    analogWrite(LED_IZQUIERDA, map(x, 0, 480, 255, 0)); //como los valores de la entrada analogica no se encuentran dentro del rango (0-255), la funcion map relaciona dichos valores con el rango de bits del arduino
    //map(variable, valor minimo que puede asumir la variable, valor maximo que puede asumir la variable,valor minimo al cual se convierte la variable, valor maximo al cual se covierte la variable)
  } else {
    analogWrite(LED_IZQUIERDA, 0); //si la condicion del if es falsa, el led se mantendra apagado
  }
  if (x >520 && x <=1023){
    analogWrite(LED_DERECHA, map(x, 520, 1023, 0, 255));
  } else {
    analogWrite(LED_DERECHA, 0);
  }
  if (y >=0 && y < 480){
    analogWrite(LED_ABAJO, map(y, 0, 480, 255, 0));
  } else {
    analogWrite(LED_ABAJO, 0);
  }
  if (y >520 && y <=1023){
    analogWrite(LED_ARRIBA, map(y, 520, 1023, 0, 255));
  } else {
    analogWrite(LED_ARRIBA, 0);
  }

  digitalWrite(LED_SW, !SW); //como el switch esta conectado directamente a una resistencia de pull-up, se tiene un valor alto en esta entrada cuando no se presiona, por lo que el (!) invierte el valor leido originalmente
}
