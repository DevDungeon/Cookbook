/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.tcpexamples.threadedserver;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author dtron
 */
public class ThreadedTcpServer {

    public static void main(String[] args) {
        // Set up server listener
        ServerSocket listener = null;
        try {
            listener = new ServerSocket(6789);
        } catch (IOException ex) {
            Logger.getLogger(ThreadedTcpServer.class.getName()).log(Level.SEVERE, null, ex);
        }

        // Handle incoming connections
        while (true) {
            try {
                Socket connectionSocket = listener.accept();
                (new ThreadedTcpServerWorker(connectionSocket)).start();
            } catch (IOException ex) {
                Logger.getLogger(ThreadedTcpServer.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }

}