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
public class SeeIfExists {

    public static void main(String[] args) {
        File homeDir = new File(System.getProperty("user.home"));
        
        System.out.println(homeDir.exists());
        System.out.println(homeDir.isDirectory());
        System.out.println(homeDir.isFile());
        
    }

}
