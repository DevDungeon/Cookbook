/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.fileexamples;

import java.io.FileOutputStream;
import java.io.IOException;

/**
 *
 * @author dtron
 */
public class WriteBinaryFile {

    public static void main(String[] args) {
        writeBinaryFile("test_binary.txt");
    }

    private static void writeBinaryFile(String fileName) {
         try {
            // Put some bytes in a buffer so we can
            // write them. Usually this would be
            // image data or something. Or it might
            // be unicode text.
            String bytes = "Hello there";
            byte[] buffer = bytes.getBytes();

            FileOutputStream outputStream = new FileOutputStream(fileName);

            // write() writes as many bytes from the buffer
            // as the length of the buffer. You can also use
            // write(buffer, offset, length) to write a specific number of
            // bytes, or only part of the buffer.
            outputStream.write(buffer);
            outputStream.close();

            System.out.println("Wrote " + buffer.length + " bytes");
        } catch (IOException ex) {
            System.out.println("Error writing file: " + fileName + "");
        }
    }

}
