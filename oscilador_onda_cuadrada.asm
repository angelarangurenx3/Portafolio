#include<p16f628a.inc>	;libreria de pic
__config 0x3f30		;palabra de configuracion

cblock 0x20		;variables globales a partir de la sram del pic

cont1
cont2
cont3
endc	;cerrar bloque de variables globales

org 0x00	;direccion de reset

inicio
;
BCF status,RP1	;RP1=0
BSF status,RP0  ;RP0=1
;entradas configuradas 1 y salidas configuradas 0
CLRF trisb		;portb es salida
;acceso al banco 0
BCF status,RP0	;RP0=0
CLRF portb	;portb inicia apagado

LED
BCF portb,0	;apagar RB0
CALL delay_1s	;retardo 1s
BSF portb,0	;encender RB0
CALL delay_1s	;retardo 1s
GOTO led
END