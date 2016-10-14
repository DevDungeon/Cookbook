/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.desktopdemo;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import javax.swing.*;

public class Main extends JFrame {

    JButton btnLaunchApplication = new JButton("Launch Application");
    JButton btnLaunchBrowser = new JButton("Launch Browser");
    JButton btnLaunchEmail = new JButton();
    JRadioButton rbEdit = new JRadioButton("Edit");
    JRadioButton rbOpen = new JRadioButton("Open", true);
    JRadioButton rbPrint = new JRadioButton("Print");
    JTextField txtBrowserURI = new JTextField();
    JTextField txtMailTo = new JTextField();
    JTextField txtFile = new JTextField();
    ButtonGroup bgAppAction = new ButtonGroup();
    JLabel lblMailRecipient = new JLabel("E-mail:");
    JLabel lblBrowserUri = new JLabel("URI:");
    JLabel lblFile = new JLabel("File:");
    JButton btnFile = new JButton("...");
    JLabel emptyLabel = new JLabel(" ");
    JPanel conLeft = new JPanel();
    JPanel conCenter = new JPanel();
    JPanel conRight = new JPanel();
    JFileChooser fc = new JFileChooser();
    File file;

    private Desktop desktop;
    private Desktop.Action action = Desktop.Action.OPEN;

    /**
     * Creates new form DesktopDemo
     */
    public Main() {
        // init all gui components
        initComponents();
        // disable buttons that launch browser, email client,
        // disable buttons that open, edit, print files
        disableActions();
        // before any Desktop APIs are used, first check whether the API is
        // supported by this particular VM on this particular host
        if (Desktop.isDesktopSupported()) {
            desktop = Desktop.getDesktop();
            // now enable buttons for actions that are supported.
            enableSupportedActions();
        }
        loadFrameIcon();
        setResizable(false);
    }

    public static void main(String args[]) {
        /* Use an appropriate Look and Feel */
        try {
            //UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
            //UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel");
            UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");
        } catch (UnsupportedLookAndFeelException ex) {
            ex.printStackTrace();
        } catch (IllegalAccessException ex) {
            ex.printStackTrace();
        } catch (InstantiationException ex) {
            ex.printStackTrace();
        } catch (ClassNotFoundException ex) {
            ex.printStackTrace();
        }
        /* Turn off metal's use of bold fonts */
        UIManager.put("swing.boldMetal", Boolean.FALSE);
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new Main().setVisible(true);
            }
        });
    }

    /**
     * Create and show components
     */
    private void initComponents() {

        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setTitle("DesktopDemo");
        txtBrowserURI.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                onLaunchBrowser(null);
            }
        });

        btnLaunchBrowser.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onLaunchBrowser(evt);
            }
        });

        txtMailTo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                onLaunchMail(null);
            }
        });

        btnLaunchEmail.setText("Launch Mail");
        btnLaunchEmail.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onLaunchMail(evt);
            }
        });

        txtFile.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                onLaunchDefaultApplication(null);
            }
        });

        rbOpen.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onOpenAction(evt);
            }
        });

        rbEdit.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onEditAction(evt);
            }
        });

        rbPrint.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onPrintAction(evt);
            }
        });

        btnLaunchApplication.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onLaunchDefaultApplication(evt);
            }
        });

        btnFile.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                onChooseFile(evt);
            }
        });

        Container conFrame = this.getContentPane();

        bgAppAction.add(rbOpen);
        bgAppAction.add(rbEdit);
        bgAppAction.add(rbPrint);

        // Components layouting
        GroupLayout layout = new GroupLayout(conFrame);
        conFrame.setLayout(layout);
        layout.setAutoCreateContainerGaps(true);
        layout.setAutoCreateGaps(true);

        GroupLayout.SequentialGroup majorHGroup = layout.createSequentialGroup();

        // Horizontal group
        GroupLayout.ParallelGroup lblHGroup
                = layout.createParallelGroup(GroupLayout.Alignment.LEADING);
        lblHGroup.addComponent(lblBrowserUri, GroupLayout.Alignment.TRAILING);
        lblHGroup.addComponent(lblMailRecipient, GroupLayout.Alignment.TRAILING);
        lblHGroup.addComponent(lblFile, GroupLayout.Alignment.TRAILING);

        GroupLayout.ParallelGroup txtFieldsHGroup
                = layout.createParallelGroup(GroupLayout.Alignment.LEADING);
        txtFieldsHGroup.addComponent(txtMailTo);
        txtFieldsHGroup.addComponent(txtBrowserURI);
        GroupLayout.SequentialGroup rbHGroup = layout.createSequentialGroup();
        rbHGroup.addComponent(rbOpen);
        rbHGroup.addComponent(rbEdit);
        rbHGroup.addComponent(rbPrint);
        txtFieldsHGroup.addGroup(rbHGroup);
        GroupLayout.SequentialGroup fileHGroup = layout.createSequentialGroup();
        fileHGroup.addComponent(txtFile);
        fileHGroup.addComponent(btnFile);
        txtFieldsHGroup.addGroup(fileHGroup);

        GroupLayout.ParallelGroup btnHGroup
                = layout.createParallelGroup(GroupLayout.Alignment.LEADING);
        btnHGroup.addComponent(btnLaunchBrowser);
        btnHGroup.addComponent(btnLaunchEmail);
        btnHGroup.addComponent(btnLaunchApplication);

        majorHGroup.addGroup(lblHGroup);
        majorHGroup.addGroup(txtFieldsHGroup);
        majorHGroup.addGroup(btnHGroup);

        layout.setHorizontalGroup(majorHGroup);

        // Vertical group
        GroupLayout.SequentialGroup majorVGroup = layout.createSequentialGroup();

        GroupLayout.ParallelGroup uriVGroup
                = layout.createParallelGroup(GroupLayout.Alignment.BASELINE);
        uriVGroup.addComponent(lblBrowserUri);
        uriVGroup.addComponent(txtBrowserURI);
        uriVGroup.addComponent(btnLaunchBrowser);

        GroupLayout.ParallelGroup mailVGroup
                = layout.createParallelGroup(GroupLayout.Alignment.BASELINE);
        mailVGroup.addComponent(lblMailRecipient);
        mailVGroup.addComponent(txtMailTo);
        mailVGroup.addComponent(btnLaunchEmail);

        GroupLayout.ParallelGroup rbVGroup
                = layout.createParallelGroup(GroupLayout.Alignment.BASELINE);
        rbVGroup.addComponent(rbOpen);
        rbVGroup.addComponent(rbEdit);
        rbVGroup.addComponent(rbPrint);

        GroupLayout.ParallelGroup fileVGroup
                = layout.createParallelGroup(GroupLayout.Alignment.BASELINE);
        fileVGroup.addComponent(lblFile);
        fileVGroup.addComponent(btnLaunchApplication);
        fileVGroup.addComponent(txtFile);
        fileVGroup.addComponent(btnFile);

        majorVGroup.addGroup(uriVGroup);
        majorVGroup.addGroup(mailVGroup);
        majorVGroup.addGroup(rbVGroup);
        majorVGroup.addGroup(fileVGroup);

        layout.setVerticalGroup(majorVGroup);

        pack();
    }

    /**
     * Load the "desktop" icon into our frame window.
     */
    private void loadFrameIcon() {
        URL imgUrl = null;
        ImageIcon imgIcon = null;

////        imgUrl = Main.class.getResource("test.gif");
////        imgIcon = new ImageIcon(imgUrl);
//        Image img = imgIcon.getImage();
//        this.setIconImage(img);
    }

    /*
     * Set the Desktop.Action to PRINT before invoking
     * the default application.
     */
    private void onPrintAction(ActionEvent evt) {
        action = Desktop.Action.PRINT;
    }

    /**
     * Set the Desktop.Action to EDIT before invoking the default application.
     */
    private void onEditAction(ActionEvent evt) {
        action = Desktop.Action.EDIT;
    }

    /**
     * Set the Desktop.Action to OPEN before invoking the default application.
     */
    private void onOpenAction(ActionEvent evt) {
        action = Desktop.Action.OPEN;
    }

    /**
     * Launch the default application associated with a specific filename using
     * the preset Desktop.Action.
     *
     */
    private void onLaunchDefaultApplication(ActionEvent evt) {
        String fileName = txtFile.getText();
        File file = new File(fileName);

        try {
            switch (action) {
                case OPEN:
                    desktop.open(file);
                    break;
                case EDIT:
                    desktop.edit(file);
                    break;
                case PRINT:
                    desktop.print(file);
                    break;
            }
        } catch (IOException ioe) {
            //ioe.printStackTrace();
            System.out.println("Cannot perform the given operation to the " + file + " file");
        }
    }

    /**
     * Launch the default email client using the "mailto" protocol and the text
     * supplied by the user.
     *
     */
    private void onLaunchMail(ActionEvent evt) {
        String mailTo = txtMailTo.getText();
        URI uriMailTo = null;
        try {
            if (mailTo.length() > 0) {
                uriMailTo = new URI("mailto", mailTo, null);
                desktop.mail(uriMailTo);
            } else {
                desktop.mail();
            }
        } catch (IOException ioe) {
            ioe.printStackTrace();
        } catch (URISyntaxException use) {
            use.printStackTrace();
        }
    }

    /**
     * Launch the default browser with the text provided by the user.
     *
     */
    private void onLaunchBrowser(ActionEvent evt) {
        URI uri = null;
        try {
            uri = new URI(txtBrowserURI.getText());
            desktop.browse(uri);
        } catch (IOException ioe) {
            System.out.println("The system cannot find the " + uri + " file specified");
            //ioe.printStackTrace();
        } catch (URISyntaxException use) {
            System.out.println("Illegal character in path");
            //use.printStackTrace();
        }
    }

    private void onChooseFile(ActionEvent evt) {
        if (evt.getSource() == btnFile) {
            int returnVal = fc.showOpenDialog(Main.this);
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                file = fc.getSelectedFile();
                txtFile.setText(file.getAbsolutePath());
            }
        }
    }

    /**
     * Enable actions that are supported on this host. The actions are: open
     * browser, open email client, and open, edit, and print files using their
     * associated application
     */
    private void enableSupportedActions() {
        if (desktop.isSupported(Desktop.Action.BROWSE)) {
            txtBrowserURI.setEnabled(true);
            btnLaunchBrowser.setEnabled(true);
        }
        if (desktop.isSupported(Desktop.Action.MAIL)) {
            txtMailTo.setEnabled(true);
            btnLaunchEmail.setEnabled(true);
        }
        if (desktop.isSupported(Desktop.Action.OPEN)) {
            rbOpen.setEnabled(true);
        }
        if (desktop.isSupported(Desktop.Action.EDIT)) {
            rbEdit.setEnabled(true);
        }
        if (desktop.isSupported(Desktop.Action.PRINT)) {
            rbPrint.setEnabled(true);
        }
        if (rbEdit.isEnabled() || rbOpen.isEnabled() || rbPrint.isEnabled()) {
            txtFile.setEnabled(true);
            btnLaunchApplication.setEnabled(true);
            btnFile.setEnabled(true);
        }
    }

    /**
     * Disable all graphical components until we know whether their
     * functionality is supported.
     */
    private void disableActions() {
        txtBrowserURI.setEnabled(false);
        btnLaunchBrowser.setEnabled(false);

        txtMailTo.setEnabled(false);
        btnLaunchEmail.setEnabled(false);

        rbEdit.setEnabled(false);
        rbOpen.setEnabled(false);
        rbPrint.setEnabled(false);

        txtFile.setEnabled(false);
        btnLaunchApplication.setEnabled(false);
        btnFile.setEnabled(false);
    }
}
