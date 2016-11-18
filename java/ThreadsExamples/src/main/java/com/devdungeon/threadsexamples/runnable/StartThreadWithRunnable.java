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
public class StartThreadWithRunnable {
    public static void main(String[] args) {
        RunnableClass runnableObject = new RunnableClass();
        Thread thread = new Thread(runnableObject);
        thread.start();
        try {
            // Join will wait for thread to finish. Without the join, execution
            // will continue immediately
            thread.join(); 
        } catch (InterruptedException ex) {
            Logger.getLogger(StartThreadWithRunnable.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("Thread complete.");
        
    }
}
