#include <MelodyUtils.h>
#include <pitches.h>



void setup()
{
MelodyUtils mel(8);
mel.Glis(NOTE_C3, NOTE_C4, 5);
delay(1000);
mel.Trem(NOTE_C3, 1000, 30);
}

void loop()
{
}
