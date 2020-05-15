#include "melody.h"
#define pin A0

void play() {
  for (int i = 0; i < sizeof(notes)/sizeof(notes[0]); i++) {
    tone(pin, notes[i], durations[i]);
    
    int pauseBetweenNotes = durations[i];
    delay(pauseBetweenNotes);

    noTone(pin);
  }
}

void setup() {
  pinMode(pin, OUTPUT);
  play();
}

void loop() {

}
