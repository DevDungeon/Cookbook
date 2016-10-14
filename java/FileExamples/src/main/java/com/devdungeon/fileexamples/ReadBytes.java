/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.fileexamples;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author dtron
 */
public class ReadBytes {
    
    public static void main(String[] args) {
        FileInputStream fileInputStream = null;
        File inputFile = new File("test.txt");
        try {
            fileInputStream = new FileInputStream(inputFile);
        } catch (FileNotFoundException ex) {
            System.out.println("Error opening file: " + inputFile.getAbsolutePath());
            Logger.getLogger(ReadBytes.class.getName()).log(Level.SEVERE, null, ex);
            System.exit(1);
        }
        byte[] bytes = new byte[8];
        
        // This offset actually determines the offset of where the values are
        // stores in the result buffer and not from the file.
        // For example offset 3 means the first 3 bytes of the result buffer
        // will not be touched. Only bytesToRead number of elements will be
        // updated too, leaving the rest of the array alone.
        int offset = 3; 
        int bytesToRead = 5;
        try {
            int bytesRead;
            bytesRead = fileInputStream.read(bytes, offset, bytesToRead);
            System.out.println("Bytes read: " + bytesRead);
            System.out.println("Data: " + Arrays.toString(bytes));
            
            bytesRead = fileInputStream.read(bytes, 4, 2);
            System.out.println("More bytes read: " + bytesRead);
            System.out.println("Data: " + Arrays.toString(bytes));
        } catch (IOException ex) {
            System.out.println("Error reading file: " + inputFile.getAbsolutePath());
            Logger.getLogger(ReadBytes.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }

}
