/*
 * The MIT License
 *
 * Copyright 2016 NanoDano <nanodano@devdungeon.com>.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package com.devdungeon.binauralaudio;

import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.SourceDataLine;

/**
 *
 * @author NanoDano <nanodano@devdungeon.com>
 */
public class PlayNoteStereo
{
    public static final int SAMPLE_RATE = 16 * 1024; // ~16KHz
    public static final int SECONDS = 6;
    public static final int NUM_CHANNELS = 2; // Stereo
    public static final int DURATION = SECONDS * 1000;
    
    public static void main(String[] args) throws LineUnavailableException
    {
        // Create audio buffers
        byte[] sinWaveLeft = new byte[SECONDS * SAMPLE_RATE];
        byte[] sinWaveRight = new byte[SECONDS * SAMPLE_RATE];
        
        final AudioFormat af = new AudioFormat(SAMPLE_RATE, 8, NUM_CHANNELS, true, true);
        SourceDataLine line;
        line = AudioSystem.getSourceDataLine(af);
        line.open(af, SAMPLE_RATE);
        line.start();

        int noteNumber = 4; // C?
        double note = ((double) noteNumber - 1) / 12d; // The chromatic note?
        
        double frequencyLeft = 440d * Math.pow(2d, note);
        double frequencyRight = 450d * Math.pow(2d, note);
        
        // Fill the buffer with a sine wave
        for (int i = 0; i < sinWaveLeft.length; i++)
        {
            double periodLeft = (double)SAMPLE_RATE / frequencyLeft;
            double angleLeft = 2.0 * Math.PI * i / periodLeft;
            
            double periodRight = (double)SAMPLE_RATE / frequencyRight;
            double angleRight = 2.0 * Math.PI * i / periodRight;
            
            sinWaveLeft[i] = (byte)(Math.sin(angleLeft) * 127f);
            sinWaveRight[i] = (byte)(Math.sin(angleRight) * 127f);
        }

        // Write the raw buffer to the output line
        play(line, sinWaveLeft, sinWaveRight, DURATION);
        
        line.drain();
        line.close();
    }

    // Write the data to the line. Interpolate the stereo channels
    private static void play(SourceDataLine line, byte[] leftAudio, byte[] rightAudio, int ms)
    {
        int length = SAMPLE_RATE * ms / 1000;
        for (int l = 0; l < length; l+=2) {
            line.write(leftAudio, l, 2);
            line.write(rightAudio, l, 2);
        }
    }
}
