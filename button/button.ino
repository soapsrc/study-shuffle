 #include <Servo.h>

Servo ser2;
int serPin2 = 10;
int serPos2 = 0;

const int buttonPin = A8;     // the number of the pushbutton pin
const int yellow =  8;      // the number of the LED pin
const int green = 7;
const int red = 6;

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  setup_sj();
  Serial.begin(9600);   
  // initialize the LED pin as an output:
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);

  ser2.attach(serPin2);
  ser2.write(serPos2);

}

bool disableButton = true;
bool disableJoystick = true;
bool buttonPressed = false;
char character;
int prevCategory = 0;

void loop() {
  int category;
  String content;

  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill 
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      content += c; //makes the string content
    } 
  }

  if (content.length() >0) {
      //Serial.println(content); //see what was received
  }

  if (content == "j")
    disableJoystick = false;
  else if (content == "d"){
    disableJoystick = true;
    disableButton = true;
    buttonPressed = false;
  }
  else if (content == "b"){
    disableButton = false;
  }
  else if (content == "g"){
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
  }
  else if (content == "r"){
    for (serPos2 = 0; serPos2 <= 180; serPos2 += 45){
      ser2.write(serPos2);
      delay(100);
    }
    digitalWrite(red, HIGH);
    digitalWrite(green, LOW);
  }

  if(!disableJoystick){
    category = loop_sj();
    if (category != 0 && !buttonPressed)
      Serial.println(category);
    prevCategory = category;
  }
    
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH && !disableButton) {
    buttonPressed = true;
    // turn LED on:
    digitalWrite(yellow, HIGH);
    for(int i = 0; i < 10; i++)
      Serial.println(1);
  } else {
    // turn LED off:
    digitalWrite(yellow, LOW);
  }
  
  delay(100);

}
