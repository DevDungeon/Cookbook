package net.electropunk.apps.cli;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author John "NanoDano" Leon <nanodano@devdungeon.com>
 */
public class FindAscii {
    
    public static void main(String[] args) {
        // Take a filename as an arg
        // print out anything ascii
        // max distance between ascii chars printed: 1 space
        String filename = args[0];
        
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
        } catch (FileNotFoundException ex) {
            Logger.getLogger(FindAscii.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
}
