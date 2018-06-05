/*
  Melody

 Plays a melody

 created 21 Jan 2010
 by Tom Igoe
 modified 21 Jan 2016
 by Yasin Kaya

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Tone

 */
#include "pitches.h"

// notes in the melody:
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int note_durations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
  // iterate over the notes of the melody:
  for (int this_note = 0; this_note < 8; this_note++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int note_duration = 1000 / note_durations[this_note];
    tone(A1, melody[this_note], note_duration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pause_between_notes = note_duration * 1.30;
    delay(pause_between_notes);
    // stop the tone playing:
    noTone(A1);
  }
}

void loop() {
  // no need to repeat the melody.
}
