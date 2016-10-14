/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.directoryexamples;

import java.io.File;

/**
 *
 * @author dtron
 */
public class CreateParentDirs {

    public static void main(String[] args) {
        // Create a directory and any required parent directories
        String homeDir = System.getProperty("user.home");
        String newFilepath = homeDir + File.separator + "tmp"
                + File.separator + "1" + File.separator + "2" + File.separator + "x.txt";
        File targetFile = new File(newFilepath);
        createParentDirs(targetFile);

    }

    private static void createParentDirs(File file) {
        File parent = file.getParentFile();
        if (!parent.exists() && !parent.mkdirs()) {
            throw new IllegalStateException("Couldn't create dir: " + parent);
        }
        System.out.println("Created: " + file.getAbsolutePath());
    }
}
