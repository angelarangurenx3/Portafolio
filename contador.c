#include <PIC16f877A.h> //se incluye la configuracion del microcontrolador PIC16F877A
#include <xc.h> //se incluye la configuracion del cristal externo

#define _XTAL_FREQ 4000000 //se define el valor del cristal en hz

void main(void) {
    TRISD = 0; //comando para conocar el puerto D como salida (0 es salida/1 es entrada)
    
    unsigned char digits[] = { //ahora se colocan los numeros en forma hexagesimal para anodo comun
        0x3F, //0
        0x06, //1
        0x5B, //2
        0x4F, //3
        0x66, //4
        0x6D, //5
        0x7D, //6
        0x07, //7
        0x7F, //8
        0x6F, //9
        //secuencia para display de anodo comun
    };
    while(1) { //se ejecutara el bucle que se repetira cuando una sentencia sea verdadera
        for(int i = 0; i <= 9; i++) {
            PORTD = ~digits[i]; //se niega la variable digits para usar un display catodo comun
            __delay_ms(1000); //retardp de 1S
        }
    }
    
    
}