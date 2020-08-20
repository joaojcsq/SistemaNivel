#include <Ultrasonic.h>

#define pino_trigger 4
#define pino_echo 5

Ultrasonic ultrasonic(pino_trigger, pino_echo);
 
void setup()
{
  Serial.begin(9600);
}
 
void loop()
{
  if(Serial.available() > 0) {
      char leitura =  Serial.read();
      if(leitura == '1'){
        float cmMsec;
        long microsec = ultrasonic.timing();
        cmMsec = ultrasonic.convert(microsec, Ultrasonic::CM);
        Serial.print(cmMsec); 
        Serial.println('f');
  }
      }
  
}
