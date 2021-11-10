// constants won't change. They're used here to set pin numbers:
const int buttonPin = A8;     // the number of the pushbutton pin
const int ledPin =  8;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  Serial.begin(9600);   
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

bool disableButton = true;
void loop() {
  String content = "";
  char character;
      
  while(Serial.available()) {
       character = Serial.read();
       content.concat(character);
  }
        
  if (content != "") {
       Serial.println("py: " + content);
  }

  if (content == "e")
    disableButton = false;
    
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH && !disableButton) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    Serial.println(1);
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
