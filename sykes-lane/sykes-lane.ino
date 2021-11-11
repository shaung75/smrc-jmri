# include <CMRI.h>

CMRI cmri;

// Define number of points
#define numPoints 16

int pointPin[numPoints*2]; // Need twice number of pins as there are points (one for close, one for throw)

void setup() {
  Serial.begin(9600, SERIAL_8N2);
  Serial.println("CMRI Sykes Lane");

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

}
