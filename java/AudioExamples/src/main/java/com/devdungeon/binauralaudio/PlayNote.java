package com.devdungeon.binauralaudio;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.SourceDataLine;

public class PlayNote 
{
    public static final int SAMPLE_RATE = 16 * 1024; // ~16KHz
    public static final int SECONDS = 3;
    
    public static void main(String[] args) throws LineUnavailableException
    {    
        final AudioFormat af =
            new AudioFormat(SAMPLE_RATE, 8, 1, true, true);
        SourceDataLine line = AudioSystem.getSourceDataLine(af);
        
        line.open(af, SAMPLE_RATE);
        line.start();
        
        int duration = 500;
        int numSeconds = 2;
        int noteNumber = 4; // C?
        
        byte[] sinWave = new byte[numSeconds * SAMPLE_RATE]; // Raw audio samples
        double exp = ((double) noteNumber - 1) / 12d;
        double f = 440d * Math.pow(2d, exp);
        
        for (int i = 0; i < sinWave.length; i++) {
            double period = (double)SAMPLE_RATE / f;
            double angle = 2.0 * Math.PI * i / period;
            sinWave[i] = (byte)(Math.sin(angle) * 127f);
        }
            
        play(line, sinWave, duration);

        line.drain();
        line.close();
    }

    private static void play(SourceDataLine line, byte[] note, int ms) {
        ms = Math.min(ms, SECONDS * 1000);
        int length = SAMPLE_RATE * ms / 1000;
        line.write(note, 0, length);
    }
}
