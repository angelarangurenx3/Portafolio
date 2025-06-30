#include <Keypad.h>

const byte FILAS = 4; //int es una variable entera de 16 bits mientras que byte tiene 8. permite almacenar valores de 0 a 255
const byte COLUMNAS = 4;
char keys [FILAS][COLUMNAS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
}; //se realiza una especie de matriz donde se mapean los valores de los botones del keypad por filas de botones
byte pinesFilas[FILAS] = {9,8,7,6}; //se realiza un array el cual es una funcion que permite alojar multiples valores a partir de un indice numerico que comienza en 0 
byte pinesColumnas[COLUMNAS] = {5,4,3,2}; //array de 4 posiciones

Keypad teclado = Keypad(makeKeymap(keys),pinesFilas,pinesColumnas,FILAS,COLUMNAS);//se crea un objeto llamado teclado de tipo Keypad y se le mapean todos los valores a partir de la funcion makeKeymap

char TECLA; //char es una variable de tipo character para que los valores ingresados en el teclado se impriman como un caracter
char CLAVE[7]; //la variable CLAVE tiene un valor de 6 digitos, pero debido al array se le agrega un digito mas
char CLAVE_MAESTRA[7] = "123456"; //la variable CLAVE_MAESTRA tiene un valor de 6 digitos, pero debido al array se le agrega un digito mas. Se usa para hacer la comparacion con CLAVE
byte INDICE = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  TECLA = teclado.getKey(); //establece los valores ingresados en el teclado
  Serial.print(TECLA); //permite ver las teclas que se presionan en el monitor serial
  if(TECLA){
    CLAVE[INDICE]=TECLA;
    INDICE++;
    Serial.print(TECLA); //en la variable TECLA se almacena el caracter que nos devuelve la funcion getKey y mas adelante se guarda en el monitor serial
  }
  if(INDICE==6){ //se pregunta si el indice llego a los 6 digitos de la contraseña
    if(!strcmp(CLAVE, CLAVE_MAESTRA)) //se verifica si la clave ingresada sí coincide con la clave maestra
    Serial.println(" Correcta"); //si el if es verdadero se imprime " Correcta"
    else
    Serial.println(" Incorrecta"); // si el if es falso se imprime " Incorrecta"
    INDICE = 0;
    // se dejan espacios en las palabras correcta e incorrecta ya que la funcion println imprime todos los valores de forma corrida
  }
}
