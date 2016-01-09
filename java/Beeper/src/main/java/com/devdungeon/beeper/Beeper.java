package com.devdungeon.beeper;


import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.border.*;
import java.text.DecimalFormat;

import javax.sound.sampled.*;

import java.io.ByteArrayInputStream;

/** Beeper presents a small, loopable tone that can be heard
by clicking on the Code Key.  It uses a Clip to loop the sound,
as well as for access to the Clip's gain control.
@author Andrew Thompson
@version 2009-12-19
@license LGPL */
public class Beeper extends JApplet {

    BeeperPanel bp;

    public void init() {
        bp = new BeeperPanel();
        getContentPane().add(bp);
        validate();

        String sampleRate = getParameter("samplerate");
        if (sampleRate!=null) {
            try {
                int sR = Integer.parseInt(sampleRate);
                bp.setSampleRate(sR);
            } catch(NumberFormatException useDefault) {
            }
        }

        String fpw = getParameter("fpw");
        if (fpw!=null) {
            try {
                int fPW = Integer.parseInt(fpw);
                JSlider slider = bp.getFramesPerWavelengthSlider();
                slider.setValue( fPW );
            } catch(NumberFormatException useDefault) {
            }
        }

        boolean harmonic = (getParameter("addharmonic")!=null);
        bp.setAddHarmonic(harmonic);

        bp.setUpSound();

        if ( getParameter("autoloop")!=null ) {
            String loopcount = getParameter("loopcount");
            if (loopcount!=null) {
                try {
                    Integer lC = Integer.parseInt(loopcount);
                    bp.loop( lC.intValue() );
                } catch(NumberFormatException doNotLoop) {
                }
            }
        }
    }

    public void stop() {
        bp.loopSound(false);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                JFrame f = new JFrame("Beeper");
                f.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
                BeeperPanel BeeperPanel = new BeeperPanel();
                f.setContentPane(BeeperPanel);
                f.pack();
                f.setMinimumSize( f.getSize() );
                f.setLocationByPlatform(true);
                f.setVisible(true);
            }
        });
    }
}