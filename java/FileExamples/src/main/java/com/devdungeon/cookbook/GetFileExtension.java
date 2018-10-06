package com.devdungeon.cookbook;

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
