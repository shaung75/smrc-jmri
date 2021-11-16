# include <CMRI.h>

CMRI cmri;

// Define number of points
#define numPoints 16
#define sensors 24

int pointPin[numPoints*2]; // Need twice number of pins as there are points (one for close, one for throw)
int sensor[sensors]; // Allocating 24 sensors

void setup() {
  Serial.begin(9600, SERIAL_8N2);
  Serial.println("CMRI Sykes Lane");

  // Set up relay pins
  // Pins 22-37 = Board 1
  // Pins 46-61 = Board 2
  int Pin = 22; // Board 1 start pin
  
  for(int i=0; i<numPoints*2; i++) {
    if(i == 16) {
      Pin = 46; // Board 2 start pin
    }

    if(i%2 == 0) {
      pointPin[i] = Pin++;
    } else {
      pointPin[i] = Pin + 7;
    }
   
    pinMode(pointPin[i], OUTPUT);
    digitalWrite(pointPin[i], HIGH);
  }

  // Set up sensor pins
  int sensorPin = 14; // Sensors start pin
  for (int i=0; i<sensors; i++) {
    sensor[i] = sensorPin++;
    
    if((i+1)%8 == 0) {
      sensorPin = sensorPin + 16;
    }
    pinMode(sensor[i], INPUT_PULLUP);
  }

}

void loop() {
  cmri.process();

  // Loop through CMRI point addresses
  for(int i=0; i<numPoints*2; i++) {
    if(cmri.get_bit(i) == 1) {
      digitalWrite(pointPin[i], LOW);
    } else {
      digitalWrite(pointPin[i], HIGH);
    }
  }

  // Process sensors
  for(int i = 0; i<sensors; i++) {
    cmri.set_bit(i, !digitalRead(sensor[i]));
  }
}
