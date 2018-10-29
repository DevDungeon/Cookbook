package net.electropunk.apps.cli;

// given a file, print out it's content in hex

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;


// alias hexprint='java -cp ~/bin/*:tools.files-1.0.0.jar com.devdungeon.tools.files.cli.HexPrint'
// alias hp='hexprint'

// Unit tests: try TDD approach/mocking if necessary, how to test cli apps

// Can take a file and output a .hex version that contains the whole file in hex format
// hex2binary reversal?

// print out only ascii bits inside a file
/**
 *
 * @author John "NanoDano" Leon <nanodano@devdungeon.com>
 */
public class HexPrint {

    // print in variable column lengths: 2,4,8,16,32,64,full
    // check args
    // print help/usage
    
    // accept stdin as an option
    
    // 
    
    public static void main(String[] args) {
        String filename = null;
        if (args.length == 0) {
            // print usage/help
            Logger.getLogger(HexPrint.class.getName()).log(Level.INFO, "No arguments provided. Exiting");
            //System.exit(-1);
            // default to something
            filename = "test.txt";
        } else {
            filename = args[0];
        }

//        System.out.printf("Dumping contents of: %s\n", filename);
        print(filename);
    }

    private static void print(String filename) {
        // Take a filename as an arg
        // print out anything ascii
        // --width=4, --width 4, --width4, -w 4, -w4
        // max distance between ascii chars printed: 1 space


        char[] buf = new char[1024];
        
        // Read through file and print it out, formatted
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            br.read(buf, 0, 1024);
            System.out.printf("%s\n", buf);
//            System.out.println(String.format("%x", buf));
            //System.out.println(String.format("%02X", new Integer(buf[3])));
            System.out.printf("%01X\n", new Integer(buf[3]));
            System.out.printf("%016x", new Integer(999999999));
            br.close();
        } catch (FileNotFoundException ex) {
            Logger.getLogger(HexPrint.class.getName()).log(Level.SEVERE, null, ex);
            // file not found: $filename
            // print usage with --help or -h or no args
        } catch (IOException ex) {
            Logger.getLogger(HexPrint.class.getName()).log(Level.SEVERE, null, ex);
        }

        
    }

}
