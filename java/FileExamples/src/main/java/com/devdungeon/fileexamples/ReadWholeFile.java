/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.fileexamples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author dtron
 */
public class ReadWholeFile {

    public static void main(String[] args) {
        byte[] bytes = null;
        bytes = readWholeFile("test.txt");
        try {
            System.out.println("Bytes: " + new String(bytes, "UTF-8"));
        } catch (UnsupportedEncodingException ex) {
            Logger.getLogger(ReadWholeFile.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    private static byte[] readWholeFile(String fileName) {
        byte[] buffer = new byte[1000];
        try {
            FileInputStream inputStream = new FileInputStream(fileName);

            // read fills buffer with data and returns
            // the number of bytes read (which of course
            // may be less than the buffer size, but
            // it will never be more).
            int total = 0;
            int nRead = 0;
            while ((nRead = inputStream.read(buffer)) != -1) {
                // Convert to String so we can display it.
                // Of course you wouldn't want to do this with
                // a 'real' binary file.
                System.out.println(new String(buffer));
                total += nRead;
            }
            inputStream.close();
            System.out.println("Read " + total + " bytes");
        } catch (FileNotFoundException ex) {
            System.out.println("Unable to open file '"+ fileName + "'");
        } catch (IOException ex) {
            System.out.println("Error reading file '"+ fileName + "'");
        }
        return buffer;
    }
}
