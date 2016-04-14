package com.devdungeon.binauralaudio;


/*File AudioPlayer02.java
Copyright 2003 Richard G. Baldwin

Demonstrates playback of an audio file.  The
path and name of the audio file is specified by
the user in a text field.

A GUI appears on the screen containing
the following components:
  Text field for the file name
  Play
  Stop

After entering an audio file name in the text
field, the user can click the Play button to
cause the program to play the audio file.  By
default, the program will play the entire file
and then get ready to play another file, or to
play the same file again.

If the user clicks the Stop button while the file
is being played, playback will terminate.
However, because the audio data is buffered in a
large buffer in the playback loop, there may be a
noticeable delay between the time that the Stop
button is clicked and the time that the playback
actually terminates.

The text field contains the default audio file
name, junk.au, when the GUI first appears on the
screen.

The program displays the format of the audio
data in the file before playing the file.  The
format is displayed on the command- line screen.

Tested using SDK 1.4.1 under Win2000
************************************************/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.sound.sampled.*;

public class AudioPlayer02 extends JFrame{

  AudioFormat audioFormat;
  AudioInputStream audioInputStream;
  SourceDataLine sourceDataLine;
  boolean stopPlayback = false;
  final JButton stopBtn = new JButton("Stop");
  final JButton playBtn = new JButton("Play");
  final JTextField textField =
                       new JTextField("junk.au");

  public static void main(String args[]){
    new AudioPlayer02();
  }//end main
  //-------------------------------------------//

  public AudioPlayer02(){//constructor

    stopBtn.setEnabled(false);
    playBtn.setEnabled(true);

    //Instantiate and register action listeners
    // on the Play and Stop buttons.
    playBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          stopBtn.setEnabled(true);
          playBtn.setEnabled(false);
          playAudio();//Play the file
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()

    stopBtn.addActionListener(
      new ActionListener(){
        public void actionPerformed(
                                  ActionEvent e){
          //Terminate playback before EOF
          stopPlayback = true;
        }//end actionPerformed
      }//end ActionListener
    );//end addActionListener()

    getContentPane().add(playBtn,"West");
    getContentPane().add(stopBtn,"East");
    getContentPane().add(textField,"North");

    setTitle("Copyright 2003, R.G.Baldwin");
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setSize(250,70);
    setVisible(true);
  }//end constructor
  //-------------------------------------------//

  //This method plays back audio data from an
  // audio file whose name is specified in the
  // text field.
  private void playAudio() {
    try{
      File soundFile =
                   new File(textField.getText());
      audioInputStream = AudioSystem.
                  getAudioInputStream(soundFile);
      audioFormat = audioInputStream.getFormat();
      System.out.println(audioFormat);

      DataLine.Info dataLineInfo =
                          new DataLine.Info(
                            SourceDataLine.class,
                                    audioFormat);

      sourceDataLine =
             (SourceDataLine)AudioSystem.getLine(
                                   dataLineInfo);

      //Create a thread to play back the data and
      // start it running.  It will run until the
      // end of file, or the Stop button is
      // clicked, whichever occurs first.
      // Because of the data buffers involved,
      // there will normally be a delay between
      // the click on the Stop button and the
      // actual termination of playback.
      new PlayThread().start();
    }catch (Exception e) {
      e.printStackTrace();
      System.exit(0);
    }//end catch
  }//end playAudio


//=============================================//
//Inner class to play back the data from the
// audio file.
class PlayThread extends Thread{
  byte tempBuffer[] = new byte[10000];

  public void run(){
    try{
      sourceDataLine.open(audioFormat);
      sourceDataLine.start();

      int cnt;
      //Keep looping until the input read method
      // returns -1 for empty stream or the
      // user clicks the Stop button causing
      // stopPlayback to switch from false to
      // true.
      while((cnt = audioInputStream.read(
           tempBuffer,0,tempBuffer.length)) != -1
                       && stopPlayback == false){
        if(cnt > 0){
          //Write data to the internal buffer of
          // the data line where it will be
          // delivered to the speaker.
          sourceDataLine.write(
                             tempBuffer, 0, cnt);
        }//end if
      }//end while
      //Block and wait for internal buffer of the
      // data line to empty.
      sourceDataLine.drain();
      sourceDataLine.close();

      //Prepare to playback another file
      stopBtn.setEnabled(false);
      playBtn.setEnabled(true);
      stopPlayback = false;
    }catch (Exception e) {
      e.printStackTrace();
      System.exit(0);
    }//end catch
  }//end run
}//end inner class PlayThread
//===================================//

}//end outer class AudioPlayer02.java