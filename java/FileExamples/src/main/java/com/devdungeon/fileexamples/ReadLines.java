/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.fileexamples;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 *
 * @author dtron
 */
public class ReadLines {

    public static void main(String[] args) {
        ArrayList lines = readLines("test.txt");
        System.out.println(lines);
    }

    private static ArrayList readLines(String fileName) {
        String line = null;
        ArrayList lines = new ArrayList();
        try {
            FileReader fileReader = new FileReader(fileName);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            while ((line = bufferedReader.readLine()) != null) {
                lines.add(line);
            }
            bufferedReader.close();
        } catch (FileNotFoundException ex) {
            System.out.println("File not found: "+ fileName);
        } catch (IOException ex) {
            System.out.println("Error reading file: " + fileName);
        }
        return lines;
    }
}
