
#include <AESLib.h>

uint8_t key[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31};
char data[] = "testing1testing2";

void setup() {
  
}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(10, HIGH);
    aes256_enc_single(key, data);
    digitalWrite(10, LOW);
    delay(1);

}
