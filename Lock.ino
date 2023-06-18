#include<Servo.h>
int com=2;
Servo lock;
void setup() {
  pinMode(com,INPUT);
  lock.attach(5);
  lock.write(0);
}

void loop() {
  
  if(digitalRead(com)==HIGH)
  {lock.write(90);}
  else
  {lock.write(0);}
}
