#include "Bridge.h"
#include "Process.h"

Process p;

void setup() {
  Serial.begin(9600);
  Bridge.begin();
  
  p.begin("/mnt/sda1/test.py");
  p.runAsynchronously();
}

void loop() {
  while (p.available() )
    Serial.print((char)p.read());
}
