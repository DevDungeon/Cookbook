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
public class GetBaseDirOfFile {
    
    public static void main(String[] args) {
        File filepath = new File("C:\\Users\\dtron\\test.txt");
        System.out.println(filepath.getParentFile().getAbsolutePath());
        // Outputs: C:\Users\dtron
    }
}
