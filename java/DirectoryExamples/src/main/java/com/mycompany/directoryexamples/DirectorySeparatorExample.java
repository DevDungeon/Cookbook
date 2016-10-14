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
public class DirectorySeparatorExample {
    public static void main(String[] args) {
        String homeDir = System.getProperty("user.home");
        String newFile = homeDir + File.separator + "temp.txt";
        System.out.println(newFile);
    }
}
