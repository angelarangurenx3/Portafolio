#include "config.h"
#include <xc.h>

#define _XTAL_FREQ 4000000

void main (void) {
    TRISD=0;
    
    unsigned char digits[] = {
        0x3F,
        0x06,
        0x5B,
        0x4F,
        0x66,
        0x6D,
        0x7D,
        0x07,
        0x7F,
        0x6F,
    };
    while(1){
        for(int i =0; i<=9; i++) {
            PORTD = ~digits[i];
            __delay_ms(1000);
        }
    }
}