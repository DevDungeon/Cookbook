/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.threadsexamples;

/**
 *
 * @author dtron
 */
public class ThreadSubclassExample extends Thread {
    public void run() {
        System.out.println("Hello from a thread!");
    }

    public static void main(String args[]) {
        (new ThreadSubclassExample()).start();
    }
}
