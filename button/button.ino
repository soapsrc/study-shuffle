const int buttonPin = A8;     // the number of the pushbutton pin
const int ledPin =  8;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  setup_sj();
  Serial.begin(9600);   
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);

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
    digitalWrite(ledPin, HIGH);
    for(int i = 0; i < 10; i++)
      Serial.println(1);
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
  digitalRead(ledPin);

  delay(100);

}
