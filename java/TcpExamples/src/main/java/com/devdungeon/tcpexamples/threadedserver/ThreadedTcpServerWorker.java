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
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author dtron
 */
public class ThreadedTcpServerWorker extends Thread {

    protected Socket connectionSocket = null;

    public ThreadedTcpServerWorker(Socket connectionSocket) {
        this.connectionSocket = connectionSocket;
    }

    public void run() {
        System.out.println("Hello from a thread!");

        try {
            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(this.connectionSocket.getInputStream()));
            DataOutputStream outToClient = new DataOutputStream(this.connectionSocket.getOutputStream());
            String clientRequest = null;

            clientRequest = inFromClient.readLine();
            System.out.println("Received from client: " + clientRequest);
            outToClient.write("HTTP/1.1 200 OK\n\n".getBytes());
            outToClient.write(clientRequest.getBytes());
            outToClient.close();
            inFromClient.close();
                    
        } catch (IOException ex) {
            Logger.getLogger(ThreadedTcpServerWorker.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
