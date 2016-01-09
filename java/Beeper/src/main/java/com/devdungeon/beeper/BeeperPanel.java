package com.devdungeon.beeper;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.ByteArrayInputStream;
import java.text.DecimalFormat;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.FloatControl;
import javax.sound.sampled.LineUnavailableException;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;
import javax.swing.border.TitledBorder;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;


/** The main UI of Beeper. */
class BeeperPanel extends JPanel {

    JComboBox sampleRate;
    JSlider framesPerWavelength;
    JLabel frequency;
    JCheckBox harmonic;
    Clip clip;

    DecimalFormat decimalFormat = new DecimalFormat("###00.00");

    BeeperPanel() {
        super(new BorderLayout());
        // Use current OS look and feel.
        try {
            UIManager.setLookAndFeel(
                UIManager.getSystemLookAndFeelClassName());
            SwingUtilities.updateComponentTreeUI(this);
        } catch (Exception e) {
            e.printStackTrace();
        }
        setPreferredSize( new Dimension(300,300) );

        JPanel options = new JPanel();
        BoxLayout bl = new BoxLayout(options,BoxLayout.Y_AXIS);
        options.setLayout(bl);

        Integer[] rates = {
            new Integer(8000),
            new Integer(11025),
            new Integer(16000),
            new Integer(22050)
        };
        sampleRate = new JComboBox(rates);
        sampleRate.setToolTipText("Samples per second");
        sampleRate.setSelectedIndex(1);
        JPanel pSampleRate = new JPanel(new BorderLayout());
        pSampleRate.setBorder(new TitledBorder("Sample Rate"));
        pSampleRate.add( sampleRate );
        sampleRate.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                setUpSound();
            }
        });
        options.add( pSampleRate );

        framesPerWavelength = new JSlider(JSlider.HORIZONTAL,10,200,25);
        framesPerWavelength.setPaintTicks(true);
        framesPerWavelength.setMajorTickSpacing(10);
        framesPerWavelength.setMinorTickSpacing(5);
        framesPerWavelength.setToolTipText("Frames per Wavelength");
        framesPerWavelength.addChangeListener( new ChangeListener(){
            public void stateChanged(ChangeEvent ce) {
                setUpSound();
            }
        } );

        JPanel pFPW = new JPanel( new BorderLayout() );
        pFPW.setBorder(new TitledBorder("Frames per Wavelength"));

        pFPW.add( framesPerWavelength );
        options.add( pFPW );

        JPanel bottomOption = new JPanel( new BorderLayout(4,4) );
        harmonic = new JCheckBox("Add Harmonic", false);
        harmonic.setToolTipText(
            "Add harmonic to second channel, one octave up");
        harmonic.addActionListener( new ActionListener(){
            public void actionPerformed(ActionEvent ae) {
                setUpSound();
            }
        } );
        bottomOption.add( harmonic, BorderLayout.WEST );

        frequency = new JLabel();
        bottomOption.add( frequency, BorderLayout.CENTER );

        options.add(bottomOption);

        add( options, BorderLayout.NORTH );

        JPanel play = new JPanel(new BorderLayout(3,3));
        play.setBorder( new EmptyBorder(4,4,4,4) );
        JButton bPlay  = new JButton("Code Key");
        bPlay.setToolTipText("Click to make tone!");
        Dimension preferredSize = bPlay.getPreferredSize();
        bPlay.setPreferredSize( new Dimension(
            (int)preferredSize.getWidth(),
            (int)preferredSize.getHeight()*3) );

        // TODO comment out to try KeyListener!
        //bPlay.setFocusable(false);
        bPlay.addKeyListener( new KeyAdapter(){
            @Override
            public void keyPressed(KeyEvent ke) {
                loopSound(true);
            }
        } );
        bPlay.addMouseListener( new MouseAdapter() {
                @Override
                public void mousePressed(MouseEvent me) {
                    loopSound(true);
                }

                @Override
                public void mouseReleased(MouseEvent me) {
                    loopSound(false);
                }
            } );
        play.add( bPlay );

        try {
            clip = AudioSystem.getClip();

            final FloatControl control = (FloatControl)
                clip.getControl( FloatControl.Type.MASTER_GAIN );

            final JSlider volume = new JSlider(
                JSlider.VERTICAL,
                (int)control.getMinimum(),
                (int)control.getMaximum(),
                (int)control.getValue()
                );
            volume.setToolTipText("Volume of beep");
            volume.addChangeListener( new ChangeListener(){
                public void stateChanged(ChangeEvent ce) {
                    control.setValue( volume.getValue() );
                }
            } );
            play.add( volume, BorderLayout.EAST );
        } catch(Exception e) {
            e.printStackTrace();
        }

        add(play, BorderLayout.CENTER);

        setUpSound();
    }

    public void loop(int loopcount) {
        if (clip!=null) {
            clip.loop( loopcount );
        }
    }

    public void setAddHarmonic(boolean addHarmonic) {
        harmonic.setSelected(addHarmonic);
    }

    /** Provides the slider for determining the # of frames per wavelength,
    primarily to allow easy adjustment by host classes. */
    public JSlider getFramesPerWavelengthSlider() {
        return framesPerWavelength;
    }

    /** Sets the sample rate to one of the four
    allowable rates. Is ignored otherwise. */
    public void setSampleRate(int sR) {
        switch (sR) {
            case 8000:
                sampleRate.setSelectedIndex(0);
                break;
            case 11025:
                sampleRate.setSelectedIndex(1);
                break;
            case 16000:
                sampleRate.setSelectedIndex(2);
                break;
            case 22050:
                sampleRate.setSelectedIndex(3);
                break;
            default:
        }
    }

    /** Sets label to current frequency settings. */
    public void setFrequencyLabel() {
        float freq = getFrequency();
        if (harmonic.isSelected()) {
            frequency.setText(
                decimalFormat.format(freq) +
                "(/" +
                decimalFormat.format(freq*2f) +
                ") Hz" );
        } else {
            frequency.setText( decimalFormat.format(freq) + " Hz" );
        }
    }

    /** Generate the tone and inform the user of settings. */
    public void setUpSound() {
        try {
            generateTone();
            setFrequencyLabel();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    /** Provides the frequency at current settings for
    sample rate & frames per wavelength. */
    public float getFrequency() {
        Integer sR = (Integer)sampleRate.getSelectedItem();
        int intST = sR.intValue();
        int intFPW = framesPerWavelength.getValue();

        return (float)intST/(float)intFPW;
    }

    /** Loops the current Clip until a commence false is passed. */
    public void loopSound(boolean commence) {
        if ( commence ) {
            clip.setFramePosition(0);
            clip.loop( Clip.LOOP_CONTINUOUSLY );
        } else {
            clip.stop();
        }
    }

    /** Generates a tone, and assigns it to the Clip. */
    public void generateTone()
        throws LineUnavailableException {
        if ( clip!=null ) {
            clip.stop();
            clip.close();
        } else {
            clip = AudioSystem.getClip();
        }
        boolean addHarmonic = harmonic.isSelected();

        int intSR = ((Integer)sampleRate.getSelectedItem()).intValue();
        int intFPW = framesPerWavelength.getValue();

        float sampleRate = (float)intSR;

        // oddly, the sound does not loop well for less than
        // around 5 or so, wavelengths
        int wavelengths = 20;
        byte[] buf = new byte[2*intFPW*wavelengths];
        AudioFormat af = new AudioFormat(
            sampleRate,
            8,  // sample size in bits
            2,  // channels
            true,  // signed
            false  // bigendian
            );

        int maxVol = 127;
        for(int i=0; i<intFPW*wavelengths; i++){
            double angle = ((float)(i*2)/((float)intFPW))*(Math.PI);
            buf[i*2]=getByteValue(angle);
            if(addHarmonic) {
                buf[(i*2)+1]=getByteValue(2*angle);
            } else {
                buf[(i*2)+1] = buf[i*2];
            }
        }

        try {
            byte[] b = buf;
            AudioInputStream ais = new AudioInputStream(
                new ByteArrayInputStream(b),
                af,
                buf.length/2 );

            clip.open( ais );
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    /** Provides the byte value for this point in the sinusoidal wave. */
    private static byte getByteValue(double angle) {
        int maxVol = 127;
        return (new Integer(
            (int)Math.round(
            Math.sin(angle)*maxVol))).
            byteValue();
    }
}