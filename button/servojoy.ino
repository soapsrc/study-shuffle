 #include <Servo.h>

Servo ser;
int serPin = 9;
int serPos = 0;

int VRx = A0;
int VRy = A1;
int SW = 2;

int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup_sj() {
  Serial.begin(9600); 
  
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  pinMode(SW, INPUT_PULLUP); 

  ser.attach(serPin);
  ser.write(serPos);
  
}

int prevPos = serPos;

void loop_sj() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);
  
  Serial.print("X: ");
  Serial.print(mapX);
  Serial.print(" | Y: ");
  Serial.print(mapY);
  Serial.print(" | Button: ");
  Serial.println(SW_state);

  // Left
  if(mapX < -500)
    serPos = 0;
  //Up
  else if(mapY > 500)
    serPos = 180;
  // Right
  else if (mapX > 500)
    serPos = 90;
  // Down
  else if(mapY < -500)
    serPos = 45;

  ser.write(serPos);

  if(prevPos != serPos)
    Serial.println(serPos);
    
  prevPos = serPos;
    

  delay(100);
  
}
