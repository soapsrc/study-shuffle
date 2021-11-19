 #include <Servo.h>

// Food dispensor servo
Servo ser2;
int serPin2 = 9;
int serPos2 = 135;

const int buttonPin = A9;   // Button that triggers random video to play 
const int yellow =  6;      // Yellow led light
const int green = 7;        // Green led light
const int red = 8;          // Red led light

int buttonState = 0;        // Variable for reading the pushbutton status

void setup() {
  // Set up the joystick and the pointing servo
  setup_sj();
  Serial.begin(9600);   
  // Initialize all LED pins as an output:
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  // Initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);

  ser2.attach(serPin2);
  ser2.write(serPos2);

}

bool disableButton = true;
bool disableJoystick = true;
bool buttonPressed = false;
char character;
int prevCategory = 0;
int greenOn = false;

void loop() {
  int category;
  String content;

  while (Serial.available()) {
    delay(3);  // Delay to allow buffer to fill 
    if (Serial.available() >0) {
      char c = Serial.read();  // Gets one byte from serial buffer
      content += c; // Concatenate the string content
    } 
  }

  if (content.length() >0) {
      //Serial.println(content); // Print what is being received
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
    greenOn = true;
    digitalWrite(green, HIGH);
    digitalWrite(red, LOW);
  }
  else if (content == "r"){
    for (serPos2 = 135; serPos2 >= 0; serPos2 -= 45){
      ser2.write(serPos2);
      delay(100);
    }
    ser2.write(135);
    digitalWrite(red, HIGH);
    digitalWrite(green, LOW);
    greenOn = false;
  }
  else if (content == "f"){
    bool on = false;
    for(int i = 0; i < 5; i++){
      if(greenOn)
        digitalWrite(green, on ? HIGH : LOW);
      else
        digitalWrite(red, on ? HIGH : LOW);
      on = !on;
      delay(500);
    }
    
  }
  // if the joystick is not disabled, get the category the arrow is pointing to
  if(!disableJoystick){
    category = loop_sj();
    if (category != 0 && !buttonPressed)
      Serial.println(category);
    prevCategory = category;
  }
    
  // Read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // Check if the pushbutton is pressed. If it is, the buttonState is HIGH
  if (buttonState == HIGH && !disableButton) {
    buttonPressed = true;
    // turn yellow LED on:
    digitalWrite(yellow, HIGH);
    // Print 1 to serial to communicate that button has been pushed
    for(int i = 0; i < 10; i++)
      Serial.println(1);
  } else {
    // turn yellow LED off:
    digitalWrite(yellow, LOW);
  }
  
  delay(100);

}
