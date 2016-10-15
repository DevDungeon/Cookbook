/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.devdungeon.tcpexamples;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 *
 * @author dtron
 */
public class TcpServerExample {

    public static void main(String[] args) throws Exception {
        ServerSocket listener = new ServerSocket(6789);

        while (true) {
            // Get the client data
            Socket connectionSocket = listener.accept();
            
            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
            DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
            String clientRequest = inFromClient.readLine();

            // Process client data and echo back respons as HTTP 200 ok
            System.out.println("Received from client: " + clientRequest);
            outToClient.write("HTTP/1.1 200 OK\n\n".getBytes());
            outToClient.writeBytes(clientRequest);
        }
    }
}
