#include <Arduino.h>

// We communicate with the power board at 115200 baud.
#define SERIAL_BAUD 115200

#define FW_VER 0

void setup() {
  Serial.begin(SERIAL_BAUD);
}

int read_pin() {
  while (!Serial.available());
  int pin = Serial.read();
  return (int)(pin - 'a');
}

void command_read() {
  int pin = read_pin();
  // Read from the expected pin.
  int level = digitalRead(pin);
  // Send back the result indicator.
  if (level == HIGH) {
    Serial.write('h');
  } else {
    Serial.write('l');
  }
}

void command_analogue_read() {
  int pin = read_pin();
  int value = analogRead(pin);
  Serial.print(value);
}

void command_write(int level) {
  int pin = read_pin();
  digitalWrite(pin, level);
}

void command_mode(int mode) {
  int pin = read_pin();
  pinMode(pin, mode);
}

int pulsePin;
int echoPin;
bool usSetup = false; //dont use pins until setup

void setup_ultrasound(){
  pulsePin = read_pin();
  echoPin = read_pin();
  pinMode(pulsePin,OUTPUT);
  digitalWrite(pulsePin,LOW);
  pinMode(echoPin,INPUT);
  delayMicroseconds(30);
  usSetup = true;
}

void read_ultrasound(){
  if(usSetup){
    unsigned long t1 = micros();
    digitalWrite(pulsePin,HIGH);
    delayMicroseconds(12);
    digitalWrite(pulsePin,LOW);
    unsigned int total;
    while((total=(micros()-t1))<25000 && digitalRead(echoPin)==LOW);

    int cm = total/58;
    Serial.print(cm);
  }else{
    Serial.print(1000);
  }
}

void loop() {
  // Fetch all commands that are in the buffer
  while (Serial.available()) {
    int selected_command = Serial.read();
    // Do something different based on what we got:
    switch (selected_command) {
      case 'a':
        command_analogue_read();
        break;
      case 'r':
        command_read();
        break;
      case 'l':
        command_write(LOW);
        break;
      case 'h':
        command_write(HIGH);
        break;
      case 'i':
        command_mode(INPUT);
        break;
      case 'o':
        command_mode(OUTPUT);
        break;
      case 'p':
        command_mode(INPUT_PULLUP);
        break;
      case 'v':
        Serial.print("SRcustom:");
        Serial.print(FW_VER);
        break;
      case 's':
        setup_ultrasound();
        break;
      case 'u':
        read_ultrasound();
        break;
      default:
        // A problem here: we do not know how to handle the command!
        // Just ignore this for now.
        break;
    }
    Serial.print("\n");
  }
}
