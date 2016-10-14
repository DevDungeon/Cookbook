/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.fileexamples;

import java.io.File;

/**
 *
 * @author dtron
 */
public class GetFileExtension {
    
    public static void main(String[] args) {
        String homeDir = System.getProperty("user.home");
        String newFilepath = homeDir + File.separator + "x" + File.separator + "test.txt";
        System.out.println(getFileExtension(newFilepath));
    }
    
    private static String getFileExtension(String filepath) {
        String[] splitFilepath = filepath.split("\\.");
        int index = splitFilepath.length -1;
        if (index < 0) {
            index = 0;
        }
        return splitFilepath[index];
    }
}
