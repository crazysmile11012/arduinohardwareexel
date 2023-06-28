char data;
String readString;
void setup() {
  Serial.begin(9600);

}

void loop() {
    while (Serial.available()) {
      delay(2);  //delay to allow byte to arrive in input buffer
      char c = Serial.read();
      readString += c;
    }

  if (readString.length() >0) {
    Serial.print(readString);

    readString="";
  } 
}
