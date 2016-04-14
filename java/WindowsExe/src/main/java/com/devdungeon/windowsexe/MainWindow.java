/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.windowsexe;

import javax.swing.JColorChooser;
import javax.swing.JDialog;

/**
 *
 * @author dtron
 */
public class MainWindow extends JDialog {
    private static final long serialVersionUID = 1L;
    private final JColorChooser cc;

    public MainWindow() {
        setSize(800, 600);
        setTitle("Test Windows Application");
        cc = new JColorChooser();
        add(cc);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        setVisible(true);
    }

    public static void main(final String[] args) {
        new MainWindow();
    }
}
