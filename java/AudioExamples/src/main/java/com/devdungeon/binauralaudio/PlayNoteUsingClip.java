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

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;

/**
 *
 * @author NanoDano <nanodano@devdungeon.com>
 */
public class PlayNoteUsingClip {
    
    Clip clip;
    
    public static void main(String[] args) {
        try {
            PlayNoteUsingClip generator = new PlayNoteUsingClip();
            generator.setupClip();
            generator.generateTone();
        } catch (LineUnavailableException ex) {
            Logger.getLogger(PlayNoteUsingClip.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    public void setupClip() {
        try {
            clip = AudioSystem.getClip();
        } catch (LineUnavailableException ex) {
            Logger.getLogger(PlayNoteUsingClip.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public void generateTone() throws LineUnavailableException
    {    
        int frequency = 440; // A = 440Hz
        float sampleRate = 16 * 1024f;  // Samples per second
        int loops = 20;
        byte[] soundBuffer = new byte[2*frequency*loops];
        int volume = 127;
        
        AudioFormat af = new AudioFormat(
            sampleRate,
            8,  // sample size in bits
            2,  // channels
            true,  // signed
            false  // bigendian
            );

        // Fill the byte buffer with the proper samples
        for (int i=0; i<frequency*loops; i++) {
            double angle = ((float)(i*2)/((float)frequency))*(Math.PI);
            soundBuffer[i*2] = new Integer((int)Math.round(Math.sin(angle)*volume)).byteValue();
        }

        // Create audio stream out of the bytes
        //byte[] b = soundBuffer; // Do I need this new one?
        AudioInputStream ais = new AudioInputStream(
            new ByteArrayInputStream(soundBuffer),
            af,
            soundBuffer.length/2 );
        
        // Have the clip object 
        try {
            clip.open( ais );
        } catch (IOException ex) {
            Logger.getLogger(PlayNoteUsingClip.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        clip.loop(100);
        

        try {
            //clip.loop(0);
            //clip.loop();
            System.out.println("Sleeping for 4 sec.");
            Thread.sleep(4000);
            
            clip.loop(0);
            
            System.out.println("Sleeping for 4 sec.");
            Thread.sleep(4000);
            
        } catch (InterruptedException ex) {
            Logger.getLogger(PlayNoteUsingClip.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
    }
}
