package com.devdungeon.binauralaudio;

/*File AudioEvents01.java
The main purpose of this program is to
demonstrate audio line event handling.

This program demonstrates the capture and
subsequent playback of audio data, and
demonstrates the instantiation and registration
of line event listeners as well.  The event
listeners display messages on the screen when
the various audio line events occur.

A GUI appears on the screen containing the
following buttons:
Capture
Stop
Playback

Input data from a microphone is captured and
saved in a ByteArrayOutputStream object when the
user clicks the Capture button.

Data capture stops when the user clicks the Stop
button.

Playback begins when the user clicks the Playback
button.

Following is the screen output following the
click on the Capture button.  Note that line
breaks were manually inserted in this, and the
other output material shown below, to cause the
material to fit this narrow format.

Event handler for TargetDataLine
Event type: Open
Line info: interface TargetDataLine supporting
 64 audio formats

Event handler for TargetDataLine
Event type: Start
Line info: interface TargetDataLine supporting
 64 audio formats



Following is the screen output following the
click on the Stop button.

Event handler for TargetDataLine
Event type: Stop
Line info: interface TargetDataLine supporting
 64 audio formats

Event handler for TargetDataLine
Event type: Close
Line info: interface TargetDataLine supporting
 64 audio formats



Following is the screen output following the
click on the Playback button.

Event handler for SourceDataLine
Event type: Open
Line info: interface SourceDataLine supporting
 8 audio formats

Event handler for SourceDataLine
Event type: Start
Line info: interface SourceDataLine supporting
 8 audio formats

Event handler for SourceDataLine
Event type: Stop
Line info: interface SourceDataLine supporting
 8 audio formats

Event handler for SourceDataLine
Event type: Close
Line info: interface SourceDataLine supporting
 8 audio formats

Tested using SDK 1.4.0 under Win2000
************************************************/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.sound.sampled.*;

public class AudioEvents01 extends JFrame{

  boolean stopCapture = false;
  ByteArrayOutputStream byteArrayOutputStream;
  AudioFormat audioFormat;
  TargetDataLine targetDataLine;
  AudioInputStream audioInputStream;
  SourceDataLine sourceDataLine;

  public static void main(String args[]){
    new AudioEvents01();
  }//end main

  public AudioEvents01(){//constructor
    final JButton captureBtn =
                          new JButton("Capture");
    final JButton stopBtn = new JButton("Stop");
    final JButton playBtn =
                         new JButton("Playback");

    captureBtn.setEnabled(true);
    stopBtn.setEnabled(false);
    playBtn.setEnabled(false);

    //Register anonymous listeners
    captureBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          captureBtn.setEnabled(false);
          stopBtn.setEnabled(true);
          playBtn.setEnabled(false);
          //Capture input data from the
          // microphone until the Stop button is
          // clicked.
          captureAudio();
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()
    getContentPane().add(captureBtn);

    stopBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          captureBtn.setEnabled(true);
          stopBtn.setEnabled(false);
          playBtn.setEnabled(true);
          //Terminate the capturing of input
          // data from the microphone.
          stopCapture = true;
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()
    getContentPane().add(stopBtn);

    playBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          //Play back all of the data that was
          // saved during capture.
          playAudio();
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()
    getContentPane().add(playBtn);

    getContentPane().setLayout(new FlowLayout());
    setTitle("Copyright 2003, R.G.Baldwin");
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setSize(250,70);
    setVisible(true);
  }//end constructor

  //This method captures audio input from a
  // microphone and saves it in a
  // ByteArrayOutputStream object.
  private void captureAudio(){
    try{
      //Get everything set up for capture
      audioFormat = getAudioFormat();
      DataLine.Info dataLineInfo =
                          new DataLine.Info(
                            TargetDataLine.class,
                            audioFormat);
      targetDataLine =
             (TargetDataLine)AudioSystem.getLine(
                                   dataLineInfo);

      //Register a line listener on the
      // TargetDataLine object
      targetDataLine.addLineListener(
        new LineListener(){
          public void update(LineEvent e){
            System.out.println(
             "Event handler for TargetDataLine");
            System.out.println(
                   "Event type: " + e.getType());
            System.out.println("Line info: " +
                      e.getLine().getLineInfo());
            System.out.println();//blank line
          }//end update
        }//end LineListener
      );//end addLineListener()

      //Create a thread to capture the
      // microphone data and start it running. It
      // will run until the Stop button is
      // clicked.
      new CaptureThread().start();
    }catch (Exception e) {
      System.out.println(e);
      System.exit(0);
    }//end catch
  }//end captureAudio method

  //This method plays back the audio
  // data that has been saved in the
  // ByteArrayOutputStream
  private void playAudio() {
    try{
      //Get everything set up for playback.
      //Get the previously-saved data into a
      // byte array object.
      byte audioData[] = byteArrayOutputStream.
                                   toByteArray();
      //Get an input stream on the byte array
      // containing the data
      InputStream byteArrayInputStream =
                        new ByteArrayInputStream(
                                      audioData);
      AudioFormat audioFormat = getAudioFormat();
      audioInputStream =
                new AudioInputStream(
                  byteArrayInputStream,
                  audioFormat,
                  audioData.length/audioFormat.
                    getFrameSize());

      DataLine.Info dataLineInfo =
                          new DataLine.Info(
                            SourceDataLine.class,
                              audioFormat);

      sourceDataLine =
             (SourceDataLine)AudioSystem.getLine(
                                   dataLineInfo);


      //Register a line listener on the
      // SourceDataLine object
      sourceDataLine.addLineListener(
        new LineListener(){
          public void update(LineEvent e){
            System.out.println(
             "Event handler for SourceDataLine");
            System.out.println(
                   "Event type: " + e.getType());
            System.out.println("Line info: "
                    + e.getLine().getLineInfo());
            System.out.println();//blank line
          }//end update
        }//end LineListener
      );//end addLineListener()

      //Create a thread to play back the data and
      // start it running.  It will run until all
      // the data has been played back, at which
      // time it will automatically stop the
      // line and fire a Stop event.
      new PlayThread().start();
    }catch (Exception e) {
      System.out.println(e);
      System.exit(0);
    }//end catch
  }//end playAudio

  //This method creates and returns an
  // AudioFormat object for a given set of format
  // parameters.  If these parameters don't work
  // well for you, try some of the other
  // allowable parameter values, which are shown
  // in comments following the declarations.
  private AudioFormat getAudioFormat(){
    float sampleRate = 8000.0F;
    //8000,11025,16000,22050,44100
    int sampleSizeInBits = 16;
    //8,16
    int channels = 1;
    //1,2
    boolean signed = true;
    //true,false
    boolean bigEndian = false;
    //true,false
    return new AudioFormat(sampleRate,
                           sampleSizeInBits,
                           channels,
                           signed,
                           bigEndian);
  }//end getAudioFormat
//=============================================//

//Inner class to capture data from microphone
class CaptureThread extends Thread{
  //An arbitrary-size temporary holding buffer
  byte tempBuffer[] = new byte[10000];
  public void run(){

    byteArrayOutputStream =
                     new ByteArrayOutputStream();
    stopCapture = false;
    try{
      targetDataLine.open(audioFormat);
      targetDataLine.start();

      //Loop until stopCapture is set by another
      // thread that services the Stop button.
      while(!stopCapture){
        //Read data from the internal buffer of
        // the data line.
        int cnt = targetDataLine.read(
                              tempBuffer,
                              0,
                              tempBuffer.length);
        if(cnt > 0){
          //Save data in output stream object.
          byteArrayOutputStream.write(
                             tempBuffer, 0, cnt);
        }//end if
      }//end while
      byteArrayOutputStream.close();

      targetDataLine.stop();
      targetDataLine.close();

    }catch (Exception e) {
      System.out.println(e);
      System.exit(0);
    }//end catch
  }//end run
}//end inner class CaptureThread
//=============================================//

//Inner class to play back the data that was
// saved.
class PlayThread extends Thread{
  byte tempBuffer[] = new byte[10000];

  public void run(){
    try{
      int cnt;

      sourceDataLine.open(audioFormat);
      sourceDataLine.start();

      //Loop until the input read method returns
      // -1 for empty stream.
      while((cnt = audioInputStream.read(
                              tempBuffer,
                              0,
                              tempBuffer.length))
                                          != -1){
        if(cnt > 0){
          //Write data to the internal buffer of
          // the data line where it will be
          // delivered to the speaker.
          sourceDataLine.write(
                             tempBuffer, 0, cnt);
        }//end if
      }//end while
      //Block and wait for internal buffer of the
      // data line to become empty.  When it
      // becomes empty, it will fire a Stop
      // event and return.
      sourceDataLine.drain();
      sourceDataLine.close();
    }catch (Exception e) {
      System.out.println(e);
      System.exit(0);
    }//end catch
  }//end run
}//end inner class PlayThread
//=============================================//

}//end outer class AudioEvents01.java