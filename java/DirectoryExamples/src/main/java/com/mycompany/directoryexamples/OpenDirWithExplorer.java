/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.directoryexamples;

import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author dtron
 */
public class OpenDirWithExplorer {

    public static void main(String[] args) {
        openUserHomeDirInExplorer();
    }
    
    private static void openUserHomeDirInExplorer() {
        File file = new File(System.getProperty("user.home"));

        Desktop desktop = Desktop.getDesktop();
        try {
            desktop.open(file);
        } catch (IOException ex) {
            Logger.getLogger(OpenDirWithExplorer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
