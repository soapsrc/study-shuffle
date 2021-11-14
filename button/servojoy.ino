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
bool servoMoved = false;

int loop_sj() {
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);
  mapX = map(xPosition, 0, 1023, -512, 512);
  mapY = map(yPosition, 0, 1023, -512, 512);
  /**
  Serial.print("X: ");
  Serial.print(mapX);
  Serial.print(" | Y: ");
  Serial.print(mapY);
  Serial.print(" | Button: ");
  Serial.println(SW_state);
  */

  int category = 0;

  // Left
  if(mapX < -500){
    serPos -= 45;
    servoMoved = true;
  }
  // Right
  else if (mapX > 500){
    serPos += 45;
    servoMoved = true;
  }

  if(serPos < 0)
    serPos = 0;
  else if(serPos>180)
    serPos = 180;

  if(serPos == 0 && servoMoved)
    category = 2;   // anime
  else if(serPos == 45)
    category = 5;   // r&b
  else if(serPos == 90)
    category = 4;   // window
  else if(serPos == 135)
    category = 6;   // white noise
  else if(serPos == 180)
    category = 3;   // beach

  ser.write(serPos);
    
  prevPos = serPos;

  delay(300);
    
  return category;
  
}
