/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.threadsexamples.runnable;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author NanoDano <nanodano@devdungeon.com>
 */
public class RunnableClass implements Runnable {
    
    public void run() {
        System.out.println("Runnable class is now running!");
        try {
            Thread.sleep(4000);
        } catch (InterruptedException ex) {
            Logger.getLogger(RunnableClass.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("Runnable thread now returning.");
    }
    
}
