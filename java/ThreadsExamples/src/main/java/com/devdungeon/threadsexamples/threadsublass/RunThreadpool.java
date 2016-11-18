/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.threadsexamples.threadsublass;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 *
 * @author NanoDano <nanodano@devdungeon.com>
 */
public class RunThreadpool {
    public static void main(String[] args) {
        runThreads();
    }
    
    private static void runThreads() {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        for (int i = 0; i < 10; i++) {
            Runnable worker = new ThreadSubclassExample();
            executor.execute(worker);
          }
        executor.shutdown();
        while (!executor.isTerminated()) {
            // Threads are still running
        }
        System.out.println("All threads complete.");
    }
}
