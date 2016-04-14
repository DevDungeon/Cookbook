package com.devdungeon.binauralaudio;

/*File AudioRecorder02.java
Copyright 2003, Richard G. Baldwin

This program demonstrates the capture of audio
data from a microphone into an audio file.

A GUI appears on the screen containing the
following buttons:
  Capture
  Stop

In addition, five radio buttons appear on the
screen allowing the user to select one of the
following five audio output file formats:

  AIFC
  AIFF
  AU
  SND
  WAVE

When the user clicks the Capture button, input
data from a microphone is captured and saved in
an audio file named junk.xx having the specified
file format.  (xx is the file extension for the
specified file format.  You can easily change the
file name to something other than junk if you
choose to do so.)

Data capture stops and the output file is closed
when the user clicks the Stop button.

It should be possible to play the audio file
using any of a variety of readily available
media players, such as the Windows Media Player.

Not all file types can be created on all systems.
For example, types AIFC and SND produce a "type
not supported" error on my system.

Be sure to release the old file from the media
player before attempting to create a new file
with the same extension.

Tested using SDK 1.4.1 under Win2000
************************************************/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.sound.sampled.*;

public class AudioRecorder02 extends JFrame{

  AudioFormat audioFormat;
  TargetDataLine targetDataLine;

  final JButton captureBtn =
                          new JButton("Capture");
  final JButton stopBtn = new JButton("Stop");

  final JPanel btnPanel = new JPanel();
  final ButtonGroup btnGroup = new ButtonGroup();
  final JRadioButton aifcBtn =
                        new JRadioButton("AIFC");
  final JRadioButton aiffBtn =
                        new JRadioButton("AIFF");
  final JRadioButton auBtn =//selected at startup
                     new JRadioButton("AU",true);
  final JRadioButton sndBtn =
                         new JRadioButton("SND");
  final JRadioButton waveBtn =
                        new JRadioButton("WAVE");

  public static void main( String args[]){
    new AudioRecorder02();
  }//end main

  public AudioRecorder02(){//constructor
    captureBtn.setEnabled(true);
    stopBtn.setEnabled(false);

    //Register anonymous listeners
    captureBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          captureBtn.setEnabled(false);
          stopBtn.setEnabled(true);
          //Capture input data from the
          // microphone until the Stop button is
          // clicked.
          captureAudio();
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()

    stopBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          captureBtn.setEnabled(true);
          stopBtn.setEnabled(false);
          //Terminate the capturing of input data
          // from the microphone.
          targetDataLine.stop();
          targetDataLine.close();
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()

    //Put the buttons in the JFrame
    getContentPane().add(captureBtn);
    getContentPane().add(stopBtn);

    //Include the radio buttons in a group
    btnGroup.add(aifcBtn);
    btnGroup.add(aiffBtn);
    btnGroup.add(auBtn);
    btnGroup.add(sndBtn);
    btnGroup.add(waveBtn);

    //Add the radio buttons to the JPanel
    btnPanel.add(aifcBtn);
    btnPanel.add(aiffBtn);
    btnPanel.add(auBtn);
    btnPanel.add(sndBtn);
    btnPanel.add(waveBtn);

    //Put the JPanel in the JFrame
    getContentPane().add(btnPanel);

    //Finish the GUI and make visible
    getContentPane().setLayout(new FlowLayout());
    setTitle("Copyright 2003, R.G.Baldwin");
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setSize(300,120);
    setVisible(true);
  }//end constructor

  //This method captures audio input from a
  // microphone and saves it in an audio file.
  private void captureAudio(){
    try{
      //Get things set up for capture
      audioFormat = getAudioFormat();
      DataLine.Info dataLineInfo =
                          new DataLine.Info(
                            TargetDataLine.class,
                            audioFormat);
      targetDataLine = (TargetDataLine)
               AudioSystem.getLine(dataLineInfo);

      //Create a thread to capture the microphone
      // data into an audio file and start the
      // thread running.  It will run until the
      // Stop button is clicked.  This method
      // will return after starting the thread.
      new CaptureThread().start();
    }catch (Exception e) {
      e.printStackTrace();
      System.exit(0);
    }//end catch
  }//end captureAudio method

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
// and write it to an output audio file.
class CaptureThread extends Thread{
  public void run(){
    AudioFileFormat.Type fileType = null;
    File audioFile = null;

    //Set the file type and the file extension
    // based on the selected radio button.
    if(aifcBtn.isSelected()){
      fileType = AudioFileFormat.Type.AIFC;
      audioFile = new File("junk.aifc");
    }else if(aiffBtn.isSelected()){
      fileType = AudioFileFormat.Type.AIFF;
      audioFile = new File("junk.aif");
    }else if(auBtn.isSelected()){
      fileType = AudioFileFormat.Type.AU;
      audioFile = new File("junk.au");
    }else if(sndBtn.isSelected()){
      fileType = AudioFileFormat.Type.SND;
      audioFile = new File("junk.snd");
    }else if(waveBtn.isSelected()){
      fileType = AudioFileFormat.Type.WAVE;
      audioFile = new File("junk.wav");
    }//end if

    try{
      targetDataLine.open(audioFormat);
      targetDataLine.start();
      AudioSystem.write(
            new AudioInputStream(targetDataLine),
            fileType,
            audioFile);
    }catch (Exception e){
      e.printStackTrace();
    }//end catch

  }//end run
}//end inner class CaptureThread
//=============================================//

}//end outer class AudioRecorder02.java