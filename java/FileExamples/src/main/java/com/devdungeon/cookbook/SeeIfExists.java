package com.devdungeon.cookbook;

import java.io.File;


/**
 *
 * @author dtron
 */
public class SeeIfExists {

    public static void main(String[] args) {
        File homeDir = new File(System.getProperty("user.home"));
        
        System.out.println(homeDir.exists());
        System.out.println(homeDir.isDirectory());
        System.out.println(homeDir.isFile());
        
    }

}
